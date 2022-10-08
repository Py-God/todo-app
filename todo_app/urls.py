from django.urls import path
from .views import (
    TaskListView,
    TaskDeleteView,
    TaskUpdateView,
    TaskCreateView,
    TaskDetailView,
)

urlpatterns = [
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("new/", TaskCreateView.as_view(), name="task_new"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("", TaskListView.as_view(), name="home"),
]
