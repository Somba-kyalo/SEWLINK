from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from CustomerApp.models import CustomerProfile
from .forms import JobForm
from .models import Job
from TailorApp.models import TailorProfile
from django.contrib import messages
from TailorApp.models import TailorProfile



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

@login_required
def tailor_job_detail(request, pk):
    tailor = get_object_or_404(TailorProfile, user=request.user)

    job = get_object_or_404(
        Job,
        pk=pk,
        status='open'
    )

    return render(
        request,
        'JobApp/tailor_job_detail.html',
        {
            'tailor': tailor,
            'job': job,
        }
    )
    
@login_required
def tailor_job_list(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)

    jobs = Job.objects.filter(
        status='open'
    ).select_related(
        'customer'
    ).order_by('-created_at')

    return render(
        request,
        'JobApp/tailor_job_list.html',
        {
            'tailor': tailor,
            'jobs': jobs,
        }
    )
    
    
@login_required
def accept_job(request, pk):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    job = get_object_or_404(Job, pk=pk, status='open')

    if request.method == 'POST':
        job.tailor = tailor
        job.status = 'accepted'
        job.save()
        messages.success(request, 'Job accepted successfully.')
        return redirect('JobApp:tailor_job_list')

    return redirect('JobApp:tailor_job_detail', pk=pk)


@login_required
def reject_job(request, pk):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    job = get_object_or_404(Job, pk=pk, status='open')

    if request.method == 'POST':
        job.tailor = tailor
        job.status = 'rejected'
        job.save()
        messages.success(request, 'Job rejected.')
        return redirect('JobApp:tailor_job_list')

    return redirect('JobApp:tailor_job_detail', pk=pk)


@login_required
def tailor_my_jobs(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    jobs = Job.objects.filter(tailor=tailor).order_by('-created_at')
    return render(request, 'JobApp/tailor_my_jobs.html', {'tailor': tailor, 'jobs': jobs})

@login_required
def start_job(request, pk):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    job = get_object_or_404(Job, pk=pk, tailor=tailor, status='accepted')

    if request.method == 'POST':
        job.status = 'in_progress'
        job.save()
        messages.success(request, 'Job started successfully.')
        return redirect('JobApp:tailor_my_jobs')

    return redirect('JobApp:tailor_my_jobs')