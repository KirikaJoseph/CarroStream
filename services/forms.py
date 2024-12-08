from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'price', 'description', 'image']
        widgets = {
            'image': forms.ClearableFileInput(), 
        }