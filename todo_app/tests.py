from django.test import TestCase
from django.urls import reverse
from .models import Task
from django.utils import timezone


class TaskListViewTests(TestCase):
    def test_homepage_at_correct_url_and_uses_correct_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_with_correct_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")


class TaskCreateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            title="Exercise", is_completed=False, time_due=timezone.now()
        )

    def test_post_model(self):
        self.assertEqual(self.task.title, "Exercise")
        self.assertEqual(str(self.task), "Exercise")
        self.assertEqual(self.task.get_absolute_url(), "/1/")
