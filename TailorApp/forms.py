from django import forms
from .models import Portfolio, Service, TailorProfile


class TailorProfileForm(forms.ModelForm):
    class Meta:
        model = TailorProfile
        fields = [
            "business_name",
            "full_name",
            "phone",
            "location",
            "profile_picture",
            "bio",
            "experience_years",
            "skills",
            "is_available",
        ]

        widgets = {
            "business_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Samuel Tailoring House",
                }
            ),
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your full name"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. 0700000000"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. Voi, Kenya"}
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Tell customers about yourself and your tailoring"
                        " business..."
                    ),
                    "rows": 5,
                }
            ),
            "experience_years": forms.NumberInput(
                attrs={"class": "form-control", "min": "0", "placeholder": "e.g. 5"}
            ),
            "skills": forms.SelectMultiple(
                attrs={"class": "form-select", "size": "6"}
            ),
            "is_available": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "starting_price", "estimated_days"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Custom Suit Making",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe the service...",
                    "rows": 5,
                }
            ),
            "starting_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. 3500",
                    "min": "0",
                }
            ),
            "estimated_days": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "e.g. 5", "min": "1"}
            ),
        }


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["title", "description", "image"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Portfolio title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe this work",
                    "rows": 5,
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }