from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'budget', 'deadline', 'location', 'reference_image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter job title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the work you need'}),
            'category': forms.Select(),
            'budget': forms.NumberInput(attrs={'placeholder': 'Your budget'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput(attrs={'placeholder': 'Where should the work be done?'}),
            'reference_image': forms.ClearableFileInput(),
        }