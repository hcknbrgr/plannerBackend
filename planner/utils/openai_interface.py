import json

import openai
from django.apps import apps


def openai_decompose(todo):
    description = todo.description
    print(f"Description: {description}")
    try:
        client = openai.OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "ELI5, Break down large tasks into smaller less than 10 subtasks. Each task should take less than six minutes. Respond in a valid JSON format with each subtask being numbered and paired with the task."
                    "{'task':'description of parent task', 'subtasks': {'1':'subtask description'}}",
                },
                {
                    "role": "user",
                    "content": f"{description}",
                },
            ],
        )

        message, subtasks = transform_response(
            completion.choices[0].message.content
        )
        # TODO: handle errors differently, 'error' could be in user request
        if "error" in message:
            return {"message": message}
        generate_subtasks(todo, subtasks)
        return {"message": "Subtasks created successfully"}
    except Exception as e:
        return [e]


def transform_response(message):
    try:
        parsed_response = json.loads(message)
        if "subtasks" not in parsed_response:
            raise ValueError("Invalid response format: Missing 'subtasks' key")
        message = parsed_response["task"]
        subtasks = parsed_response["subtasks"]
    except json.JSONDecodeError as e:
        return "JSON Decode Error", str(e)
    except KeyError as e:
        return "Key Error", str(e)
    return message, subtasks


def generate_subtasks(todo, subtasks):
    s = []
    Subtask = apps.get_model("planner", "Subtask")
    for key, value in subtasks.items():
        s.append(Subtask(todo=todo, step=int(key), description=value))
    Subtask.objects.bulk_create(s)
