from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=39)
    descrption = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title