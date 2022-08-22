from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'home.html'

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'task_delete.html'
    success_url = reverse_lazy('home')

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'task_edit.html'
    fields = ('title',)

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'task_new.html'
    fields = ('title',)
