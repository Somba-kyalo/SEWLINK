from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(request, 'TailorApp/tailor_dashboard.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ServiceForm
from .models import Service, TailorProfile


@login_required
def services(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    service_list = Service.objects.filter(tailor=tailor)
    return render(request, 'TailorApp/services.html', {'services': service_list})


@login_required
def service_create(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)

    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            service.tailor = tailor
            service.save()
            return redirect('TailorApp:services')

    else:
        form = ServiceForm()

    return render(request, 'TailorApp/service_create.html', {'form': form})


@login_required
def service_edit(request, service_id):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    service = get_object_or_404(Service, id=service_id, tailor=tailor)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)

        if form.is_valid():
            form.save()
            return redirect('TailorApp:services')

    else:
        form = ServiceForm(instance=service)

    return render(request, 'TailorApp/service_edit.html', {'form': form, 'service': service})


@login_required
def service_delete(request, service_id):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    service = get_object_or_404(Service, id=service_id, tailor=tailor)

    if request.method == 'POST':
        service.delete()
        return redirect('TailorApp:services')

    return render(request, 'TailorApp/service_delete.html', {'service': service})