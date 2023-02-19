from django.db import models
from django.utils import timezone

class Todo(models.Model):
    task_name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    task_added_at = models.DateTimeField(default=timezone.now)
    task_updated_at = models.DateTimeField(auto_now=True)   #auto updates the time on creation and modification

    def __str__(self):
        return self.task_name