from rest_framework import serializers

from planner.models.subtask.subtask import Subtask


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = (
            "id",
            "todo",
            "step",
            "description",
            "completed",
            "completed_at",
        )
