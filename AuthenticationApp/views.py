from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from CustomerApp.models import CustomerProfile
from TailorApp.models import TailorProfile

from .forms import LoginForm, RegistrationForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect('AuthenticationApp:dashboard_redirect')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            account_type = form.cleaned_data['account_type']

            if account_type == 'customer':
                CustomerProfile.objects.create(
                    user=user,
                    full_name=user.username,
                )

            elif account_type == 'tailor':
                TailorProfile.objects.create(
                    user=user,
                    full_name=user.username,
                    business_name=f"{user.username}'s Tailoring",
                )

            login(request, user)

            return redirect(
                'AuthenticationApp:dashboard_redirect'
            )

    else:
        form = RegistrationForm()

    return render(
        request,
        'AuthenticationApp/register.html',
        {'form': form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('AuthenticationApp:dashboard_redirect')

    if request.method == 'POST':
        form = LoginForm(
            request=request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()

            login(request, user)

            return redirect(
                'AuthenticationApp:dashboard_redirect'
            )

    else:
        form = LoginForm()

    return render(
        request,
        'AuthenticationApp/login.html',
        {'form': form}
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect('AuthenticationApp:login')


@login_required
def dashboard_redirect(request):

    user = request.user

    if hasattr(user, 'customer_profile'):
        return redirect('CustomerApp:dashboard')

    if hasattr(user, 'tailor_profile'):
        return redirect('TailorApp:dashboard')

    logout(request)

    return redirect('AuthenticationApp:login')