from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomerProfileForm

@login_required
def dashboard(request):
    return render(request, 'CustomerApp/customer_dashboard.html')

@login_required
def profile(request):
    customer_profile = request.user.customer_profile

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=customer_profile)

        if form.is_valid():
            form.save()
            return redirect('CustomerApp:profile')
    else:
        form = CustomerProfileForm(instance=customer_profile)

    return render(request, 'CustomerApp/customer_profile.html', {'form': form, 'customer_profile': customer_profile})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import models
from .forms import CustomerProfileForm
from TailorApp.models import TailorProfile

@login_required
def dashboard(request):
    return render(request, 'CustomerApp/customer_dashboard.html')

@login_required
def profile(request):
    customer_profile = request.user.customer_profile

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=customer_profile)

        if form.is_valid():
            form.save()
            return redirect('CustomerApp:profile')
    else:
        form = CustomerProfileForm(instance=customer_profile)

    return render(request, 'CustomerApp/customer_profile.html', {'form': form, 'customer_profile': customer_profile})

@login_required
def tailor_search(request):
    query = request.GET.get('q', '').strip()

    tailors = TailorProfile.objects.all().order_by('-created_at')

    if query:
        tailors = tailors.filter(
            models.Q(business_name__icontains=query) |
            models.Q(full_name__icontains=query) |
            models.Q(location__icontains=query)
        )

    return render(request, 'CustomerApp/tailor_search.html', {'tailors': tailors, 'query': query})