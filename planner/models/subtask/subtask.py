from django.db import models

from planner.models.todo.todo import Todo

# A Subtask may have one Todo, and one Todo may have many Subtasks


class Subtask(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    step = models.IntegerField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["step"]

    def __str__(self):
        return str(self.step) + ": " + str(self.description)
