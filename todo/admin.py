from django.contrib import admin
from todo.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status', 'task_added_at', 'task_updated_at')

admin.site.register(Todo, TodoAdmin)