from rest_framework import serializers

from planner.models import todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ("id", "title", "description", "completed")
