import pytest
from pytest_factoryboy import register

from planner.testing.factories import SubtaskFactory
from planner.testing.factories import TodoFactory

register(TodoFactory)
register(SubtaskFactory)


@pytest.fixture()
def todo(todo_factory):
    return todo_factory()


@pytest.fixture()
def subtask(subtask_factory):
    return subtask_factory()
