from django import forms
from .models import TailorProfile, Service, Portfolio


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'starting_price', 'estimated_days']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Custom Suit Making'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the service...', 'rows': 5}),
            'starting_price': forms.NumberInput(attrs={'placeholder': 'e.g. 3500', 'min': '0'}),
            'estimated_days': forms.NumberInput(attrs={'placeholder': 'e.g. 5', 'min': '1'}),
        }
        

from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Portfolio title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe this work', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }