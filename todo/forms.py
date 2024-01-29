from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets={
            'deadline': forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'}),
            'priority': forms.TextInput(attrs={'placeholder': 'select value 1-5'}),
        }
