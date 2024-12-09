import pytest
from pytest_factoryboy import register

from planner.testing.factories import (
    TodoFactory,
)

register(TodoFactory)


@pytest.fixture()
def todo(todo_factory):
    return todo_factory()
