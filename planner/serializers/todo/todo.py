from rest_framework import serializers

from planner.models.todo.todo import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "description", "completed")
