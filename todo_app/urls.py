from django.urls import path
from .views import (TodoListView,
                    TodoDeleteView,
                    TodoUpdateView,
                    TodoCreateView,)

urlpatterns = [
    path('new/', TodoCreateView.as_view(), name='task_new'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/edit/', TodoUpdateView.as_view(), name='task_edit'),
    path('', TodoListView.as_view(), name='home'),
]