from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Task
from .forms import TaskForm, TaskFormCreate
from django.urls import reverse_lazy
# Create your views here.

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

class HomeView(TemplateView):
    
    template_name = 'tasks/home.html'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_edit.html"
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        # adicionar logica se necessário
        return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_del.html"
    success_url = reverse_lazy('task-list')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskFormCreate
    template_name = "tasks/task_add.html"
    success_url = reverse_lazy('task-list')

