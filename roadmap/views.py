from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    task_todo = tasks.filter(status='todo')
    task_in_progress = tasks.filter(status='in_progress')
    task_done = tasks.filter(status='done')

    context = {
        'tasks': tasks,
        'task_form': TaskForm,
        'is_admin': request.user.is_superuser,
        'task_todo': task_todo,
        'task_in_progress': task_in_progress,
        'task_done': task_done,
    }

    return render(request, 'roadmap.html', context)


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

@login_required
def actualizar_tarea_estado(request):
    if request.method == 'POST':
        id_tarea = request.POST.get('id')
        columna_destino = request.POST.get('id_status')
        try:
            tarea = Task.objects.get(pk=id_tarea)
            tarea.status = columna_destino
            tarea.save()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error'})
    else:
        return JsonResponse({'status': 'error'})