# Generated by Django 5.1.1 on 2024-12-13 03:05
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("planner", "0001_add_todo_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subtask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("step", models.IntegerField()),
                ("description", models.TextField()),
                ("completed", models.BooleanField(default=False)),
                ("completed_at", models.DateTimeField()),
                (
                    "todo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="planner.todo",
                    ),
                ),
            ],
        ),
    ]
