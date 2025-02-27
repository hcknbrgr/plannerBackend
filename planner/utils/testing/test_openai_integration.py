import pytest

from planner.models.subtask.subtask import Subtask
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
    _, subtasks = transform_response(response)
    td = todo_factory(description="Break this task into subtasks")

    # generate_subtasks(td, subtasks)

    assert Subtask.objects.filter(todo=td).exists()
    assert Subtask.objects.filter(todo=td).count() == 2


# @pytest.mark.django_db
# def test_openai_integration(subtask_factory):
#     # description = "testing in django"

#     task, subtasks = transform_response(response)
#     step = next(iter(subtasks))
#     out1 = subtask_factory(step=step, description=subtasks[step])
#     step = list(subtasks.keys())[1]
#     out2 = subtask_factory(step=step, description=subtasks[step])

#     assert expected_out_task == task
#     assert expected_out_step_1 == out1.step
#     assert expected_out_desc_1 == out1.description
#     assert expected_out_step_2 == out2.step
#     assert expected_out_desc_2 == out2.description
