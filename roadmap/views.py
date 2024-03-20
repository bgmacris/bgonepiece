from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'roadmap.html', {'tasks': tasks, 'task_form': TaskForm, 'is_admin': request.user.is_superuser})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roadmap')
    else:
        form = TaskForm()
    return redirect('roadmap')