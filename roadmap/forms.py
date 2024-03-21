from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'timeline_date', 'assigned_user', 'comment', 'priority', 'start_date', 'end_date', 'tags']
        widgets = {
            'status': forms.Select(choices=Task.STATUS_CHOICES),
            'priority': forms.Select(choices=Task.PRIORITY_CHOICES),
            'tags': forms.Select(choices=Task.TAG_CHOICES),
            'timeline_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }