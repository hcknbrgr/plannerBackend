import openai


def break_down_task(description):
    try:
        client = openai.OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "ELI5, Break down large tasks into smaller less than 10 subtasks. Each task should take less than six minutes. Respond in a consistent JSON format with each subtask being numbered and paired with the task.",
                },
                {
                    "role": "user",
                    "content": "Break this task into subtasks: {description}",
                },
            ],
        )
        return completion.choices[0].message
    except Exception as e:
        return [e]
