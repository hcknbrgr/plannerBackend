from django.contrib import admin

from .subtask import Subtask


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = (
        "step",
        "description",
        "completed",
        "completed_at",
    )
