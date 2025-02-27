import pytest

from planner.models.subtask.subtask import Subtask


@pytest.mark.django_db
def test_subtask_creation(subtask_factory):
    subtask = subtask_factory()

    assert subtask.step is not None
    assert subtask.description is not None
    assert subtask.todo is not None


@pytest.mark.django_db
def test_subtask_test_case(todo_factory):
    td = todo_factory()
    subtask = Subtask.objects.create(todo=td, step=1, description="desc")

    assert subtask.todo == td
    assert subtask.step == 1
    assert subtask.description == "desc"
