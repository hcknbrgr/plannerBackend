from django.apps import apps
from django.db import models

from planner.utils import openai_interface


class Todo(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    # def add_subtasks(self, subtasks):
    #     for task in subtasks:
    #         Subtask.objects.create(todo=self, description=subtasks)

    def __str__(self):
        return self.title

    def generate_subtasks(self):
        """Generate subtasks using openAI interface"""
        Subtask = apps.get_model("planner.subtask")
        subtasks = openai_interface.openai_decompose(self.description)
        _, transformed_subtasks = openai_interface.transform_response(subtasks)
        for step, subtask_description in transformed_subtasks.items():
            subtask = Subtask.objects.create(
                todo=self, step=step, description=subtask_description
            )
        return subtask
