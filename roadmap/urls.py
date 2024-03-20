from django.urls import path

from .views import index, create_task

urlpatterns = [
    path("roadmap/", index, name="roadmap"),
    path('roadmap/create_task/', create_task, name='create_task'),
]