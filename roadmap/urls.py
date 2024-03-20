from django.urls import path

from .views import index

urlpatterns = [
    path("roadmap/", index, name="roadmap")
]