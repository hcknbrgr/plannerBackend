import pytest

from planner.models.subtask.subtask import Subtask
from planner.utils.openai_interface import generate_subtasks
from planner.utils.openai_interface import transform_response

response = """
    {
        "task": "Break this task into subtasks",
        "subtasks": {
            "1": "Identify the main components of the task",
            "2": "Divide the task into smaller logical steps"
        }
    }"""


@pytest.mark.django_db
def test_transformed_response(todo_factory):
    """Ensure responses are broken down from openai response"""
    task, subtasks = transform_response(response)
    td = todo_factory(description="Break this task into subtasks")
    expected_subtasks = {
        "1": "Identify the main components of the task",
        "2": "Divide the task into smaller logical steps",
    }

    assert task == td.description
    assert subtasks == expected_subtasks


@pytest.mark.django_db
def test_create_subtasks(todo_factory):
    """ensure subtasks are generated correctly with response and linked to Todo object"""
    _, subtasks = transform_response(response)
    td = todo_factory(description="Break this task into subtasks")

    generate_subtasks(td, subtasks)

    assert Subtask.objects.filter(todo=td).exists()
    assert Subtask.objects.filter(todo=td).count() == 2
