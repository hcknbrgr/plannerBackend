from django.contrib import admin

from planner.models.todo.todo import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")


admin.site.register(Todo, TodoAdmin)
