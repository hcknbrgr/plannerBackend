# from django.shortcuts import render
from rest_framework import viewsets

from planner.models.todo.todo import Todo
from planner.serializers.todo import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
