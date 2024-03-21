from django.urls import path

from .views import index, create_task, actualizar_tarea_estado

urlpatterns = [
    path("roadmap/", index, name="roadmap"),
    path('roadmap/create_task/', create_task, name='create_task'),
    path('actualizar_tarea_estado/', actualizar_tarea_estado, name='actualizar_tarea_estado'),
]