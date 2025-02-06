# from django.shortcuts import render
from rest_framework import viewsets

from planner.models.subtask.subtask import Subtask
from planner.models.todo.todo import Todo
from planner.serializers.subtask.subtask import SubtaskSerializer
from planner.serializers.todo.todo import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class SubtaskView(viewsets.ModelViewSet):
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()
