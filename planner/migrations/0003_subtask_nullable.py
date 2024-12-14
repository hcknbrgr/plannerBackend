# Generated by Django 5.1.1 on 2024-12-13 03:35
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("planner", "0002_add_subtask"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subtask",
            options={"ordering": ["step"]},
        ),
        migrations.AlterField(
            model_name="subtask",
            name="completed_at",
            field=models.DateTimeField(null=True),
        ),
    ]