import pytest
from django.urls import reverse
from rest_framework.test import APIClient

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
