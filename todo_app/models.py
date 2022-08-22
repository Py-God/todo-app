from django.db import models
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")