import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from planner.models.subtask.subtask import Subtask
from planner.models.todo.todo import Todo


@pytest.mark.django_db
def test_create_todo():
    """Create a test todo item using the API"""
    client = APIClient()
    url = reverse("todo-list")

    payload = {
        "title": "This is a test item.",
        "description": "testing in pytest",
    }
    r = client.post(url, payload, format="json")

    assert r.status_code == 201
    assert r.json()["title"] == "This is a test item."
    assert Todo.objects.count() == 1
    assert Todo.objects.first().description == "testing in pytest"


def test_create_todo_empty_title():
    """ensure the title is filled out"""
    client = APIClient()
    url = reverse("todo-list")

    payload = {
        "title": "",
        "description": "empty title",
    }
    r = client.post(url, payload, format="json")

    assert r.status_code == 400
    assert "title" in r.json()


@pytest.mark.django_db
def test_generate_subtasks(todo_factory):
    client = APIClient()
    todo_item = todo_factory(title="break down")

    url = reverse("generate_subtasks", args=[todo_item.id])
    r = client.post(url)

    assert r.status_code == 200
    assert Subtask.objects.filter(todo_item=todo_item).exists()
