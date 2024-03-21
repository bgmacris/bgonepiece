from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'Por Hacer'),
        ('in_progress', 'En Progreso'),
        ('done', 'Hecho')
    )
    
    TAG_CHOICES = (
        ('planificacion', 'Planificación'),
        ('bug', 'Bug'),
        ('desarrollo', 'Desarrollo'),
        ('despliegue', 'Despliegue'),
        ('test', 'Test')
    )

    PRIORITY_CHOICES = (
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta')
    )

    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    timeline_date = models.DateField()
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    priority = models.CharField(default='low', max_length=15)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=20, choices=TAG_CHOICES, blank=True)
