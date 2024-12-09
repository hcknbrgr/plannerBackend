import pytest

# from planner.models.todo.todo import Todo

# from planner.testing.factories import TodoFactory


@pytest.mark.django_db
def test_todo_creation_incomplete(todo_factory):
    """Test creation of a todo list item, incomplete"""
    td = todo_factory()
    assert td.title is not None
    assert td.description is not None
    assert not td.completed


@pytest.mark.django_db
def test_todo_creation_complete(todo_factory):
    """Test creation of a todo list item, completed"""
    td = todo_factory(completed=True)
    assert td.completed
