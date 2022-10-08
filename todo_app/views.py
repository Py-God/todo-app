from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.admin.widgets import AdminDateWidget


class TaskListView(ListView):
    model = Task
    template_name = "home.html"

    def get_queryset(self):
        return Task.objects.order_by("time_due")


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("home")


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_edit.html"
    fields = ("title", "time_due", "is_completed")

    def get_form(self, form_class=None):
        form = super(TaskUpdateView, self).get_form(form_class)
        form.fields["time_due"].widget = AdminDateWidget(attrs={"type": "date"})
        return form


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_new.html"
    fields = ("title", "time_due", "is_completed")

    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        form.fields["time_due"].widget = AdminDateWidget(attrs={"type": "date"})
        return form
