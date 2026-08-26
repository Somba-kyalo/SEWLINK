from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models

from .forms import CustomerProfileForm
from .models import CustomerProfile
from TailorApp.models import TailorProfile
from JobApp.models import Job

@login_required
def dashboard(request):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    jobs = Job.objects.filter(customer=customer)
    active_jobs = jobs.exclude(status__in=['completed', 'cancelled']).count()
    completed_jobs = jobs.filter(status='completed').count()

    return render(request, 'CustomerApp/customer_dashboard.html', {
        'customer': customer,
        'active_jobs': active_jobs,
        'completed_jobs': completed_jobs,
    })


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


@login_required
def tailor_detail(request, tailor_id):
    tailor = get_object_or_404(TailorProfile, id=tailor_id)

    return render(request, 'CustomerApp/tailor_detail.html', {'tailor': tailor})

@login_required
def dashboard(request):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    jobs = Job.objects.filter(customer=customer)
    active_jobs = jobs.exclude(status__in=['completed', 'cancelled']).count()
    completed_jobs = jobs.filter(status='completed').count()
    recent_jobs = jobs.order_by('-created_at')[:5]

    return render(request, 'CustomerApp/customer_dashboard.html', {
        'customer': customer,
        'active_jobs': active_jobs,
        'completed_jobs': completed_jobs,
        'recent_jobs': recent_jobs,
    })