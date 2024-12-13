from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    # def add_subtasks(self, subtasks):
    #     for task in subtasks:
    #         Subtask.objects.create(todo=self, description=subtasks)

    def __str__(self):
        return self.title
