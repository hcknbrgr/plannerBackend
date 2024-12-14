import json

import pytest


@pytest.mark.django_db
def test_openai_integration(subtask_factory):
    # description = "testing in django"
    response = """
    {
        "task": "Break this task into subtasks",
        "subtasks": {
            "1": "Identify the main components of the task",
            "2": "Divide the task into smaller logical steps"
        }
    }"""
    parsed_response = json.loads(response)
    task = parsed_response["task"]
    subtasks = parsed_response["subtasks"]
    step = next(iter(subtasks))
    out1 = subtask_factory(step=step, description=subtasks[step])
    step = list(subtasks.keys())[1]
    out2 = subtask_factory(step=step, description=subtasks[step])

    expected_out_task = "Break this task into subtasks"
    expected_out_step_1 = "1"
    expected_out_desc_1 = "Identify the main components of the task"
    expected_out_step_2 = "2"
    expected_out_desc_2 = "Divide the task into smaller logical steps"

    assert expected_out_task == task
    assert expected_out_step_1 == out1.step
    assert expected_out_desc_1 == out1.description
    assert expected_out_step_2 == out2.step
    assert expected_out_desc_2 == out2.description
