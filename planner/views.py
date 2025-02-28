from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from planner.models.subtask.subtask import Subtask
from planner.models.todo.todo import Todo
from planner.serializers.subtask.subtask import SubtaskSerializer
from planner.serializers.todo.todo import TodoSerializer
from planner.utils import openai_interface


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    @action(detail=True, methods=["post"])
    def generate_subtasks(self, request, pk=None):
        try:
            todo_obj = Todo.objects.get(id=pk)
            r = openai_interface.openai_decompose(todo_obj.description)
            _, subtasks = openai_interface.transform_response(r)
            openai_interface.generate_subtasks(todo_obj, subtasks)
            return JsonResponse(
                {"message": "Subtasks created successfully"}, status=200
            )
        except Todo.DoesNotExist:
            return JsonResponse({"error": "Todo item not found"}, status=404)


class SubtaskView(viewsets.ModelViewSet):
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()
