import pytest


@pytest.mark.django_db
def test_subtask_creation(subtask_factory):
    subtask = subtask_factory()

    assert subtask.step is not None
    assert subtask.description is not None
    assert subtask.todo is not None
