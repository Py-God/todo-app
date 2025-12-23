from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User # Imported the built-in User model

class Task(models.Model):
    # Link the task to a specific user (Multi-tenancy)
    # on_delete=models.CASCADE means if the User is deleted, delete their tasks too.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    title = models.CharField(max_length=140)
    is_completed = models.BooleanField(default=False) # Added a default value
    time_due = models.DateTimeField()
    
    # Audit fields (Standard Backend Practice)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Orders tasks by due date automatically when querying
        ordering = ['time_due'] 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})

    @property
    def is_overdue(self):
        """Checks if the task due date has passed."""
        # Simplified logic: strictly compare the timestamps
        return timezone.now() > self.time_due
