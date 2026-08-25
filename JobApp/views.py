from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from CustomerApp.models import CustomerProfile
from .forms import JobForm
from .models import Job


@login_required
def job_list(request):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    jobs = Job.objects.filter(customer=customer).order_by('-created_at')
    return render(request, 'JobApp/job_list.html', {'customer': customer, 'jobs': jobs})

@login_required
def job_create(request):
    customer = get_object_or_404(CustomerProfile, user=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)

        if form.is_valid():
            job = form.save(commit=False)
            job.customer = customer
            job.save()
            return redirect('JobApp:job_list')
    else:
        form = JobForm()

    return render(request, 'JobApp/create_job.html', {'form': form, 'customer': customer})


@login_required
def job_detail(request, pk):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    job = get_object_or_404(Job, pk=pk, customer=customer)

    return render(request, 'JobApp/job_detail.html', {'job': job, 'customer': customer})


@login_required
def job_update(request, pk):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    job = get_object_or_404(Job, pk=pk, customer=customer)

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)

        if form.is_valid():
            form.save()
            return redirect('JobApp:job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)

    return render(request, 'JobApp/edit_job.html', {'form': form, 'job': job, 'customer': customer})


@login_required
def job_delete(request, pk):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    job = get_object_or_404(Job, pk=pk, customer=customer)

    if request.method == 'POST':
        job.delete()
        return redirect('JobApp:job_list')

    return render(request, 'JobApp/job_detail.html', {'job': job, 'customer': customer, 'delete_confirm': True})