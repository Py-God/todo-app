from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


class Task(models.Model):
    title = models.CharField(max_length=140)
    is_completed = models.BooleanField()
    time_due = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})

    def task_expired(self):
        now = timezone.now()
        if self.time_due - now <= datetime.timedelta(
            weeks=0, days=0, hours=0, minutes=0, seconds=0, milliseconds=0
        ):
            return True
