from django.contrib import admin

from planner.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")


admin.site.register(Todo, TodoAdmin)
