import factory.fuzzy

from planner.models.subtask.subtask import Subtask
from planner.models.todo.todo import Todo


class TodoFactory(factory.django.DjangoModelFactory):

    title = factory.Faker("name")
    description = factory.Faker("sentence")
    # completed = factory.fuzzy.FuzzyChoice(choices=[True, False])

    class Meta:
        model = Todo


class SubtaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subtask

    todo = factory.SubFactory(TodoFactory)
    step = factory.Faker("pyint", min_value=1, max_value=10)
    description = factory.Faker("sentence")
    completed = False
