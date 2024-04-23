from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Task
from .forms import TaskForm, TaskFormCreate
from django.urls import reverse_lazy
import requests
# Create your views here.

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        query_set =  super().get_queryset()
        status = self.request.GET.get('status')

        if status:
            query_set = query_set.filter(status=status)
        return query_set


class HomeView(View):
    
    template_name = 'tasks/home.html'
    def get(self, request, *args, **kwargs):
        # ip = get_client_ip(request)
        ip = '170.244.78.204'
        cidade = get_location(ip)
        weather_data = get_weather_data(cidade)
        return render(request, 'tasks/home.html', {'weather_data': weather_data, 'cidade': cidade})

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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# ip = '170.244.78.204'
def get_location(ip):
    YOUR_ACCESS_KEY = '4b25b7d068d90fd4511ec360d0ae67c4'
    response = requests.get(f'http://api.ipstack.com/{ip}?access_key={YOUR_ACCESS_KEY}')
    geodata = response.json()
    return geodata['city']

def get_weather_data(cidade):
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=dd8102c525204cbb900230149243103&q={cidade}')
    weather_data = response.json()
    return weather_data['current']