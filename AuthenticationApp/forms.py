from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    ACCOUNT_TYPES = [
        ('customer', 'Customer'),
        ('tailor', 'Tailor'),
    ]

    email = forms.EmailField(required=True)

    account_type = forms.ChoiceField(
        choices=ACCOUNT_TYPES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'account_type',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email