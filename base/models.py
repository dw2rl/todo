# Imports
from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
