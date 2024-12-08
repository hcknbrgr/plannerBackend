from django.contrib import admin

from .todo import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")
