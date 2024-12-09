import factory.fuzzy

from planner.models.todo.todo import Todo


class TodoFactory(factory.django.DjangoModelFactory):

    title = factory.Faker("name")
    description = factory.Faker("sentence")
    # completed = factory.fuzzy.FuzzyChoice(choices=[True, False])

    class Meta:
        model = Todo
