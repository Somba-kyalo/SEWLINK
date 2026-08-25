from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PortfolioForm, ServiceForm
from .models import Portfolio, Service, TailorProfile


@login_required
def dashboard(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    return render(request, 'TailorApp/tailor_dashboard.html', {'tailor': tailor})


@login_required
def services(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    services = Service.objects.filter(tailor=tailor)
    return render(request, 'TailorApp/services.html', {'tailor': tailor, 'services': services})


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

    return render(request, 'TailorApp/service_form.html', {'form': form, 'tailor': tailor})


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

    return render(request, 'TailorApp/service_form.html', {'form': form, 'service': service, 'tailor': tailor})


@login_required
def service_delete(request, service_id):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    service = get_object_or_404(Service, id=service_id, tailor=tailor)

    if request.method == 'POST':
        service.delete()
        return redirect('TailorApp:services')

    return render(request, 'TailorApp/service_confirm_delete.html', {'service': service, 'tailor': tailor})

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PortfolioForm, ServiceForm
from .models import Portfolio, Service, TailorProfile


@login_required
def dashboard(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    return render(request, 'TailorApp/tailor_dashboard.html', {'tailor': tailor})


@login_required
def services(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    services = Service.objects.filter(tailor=tailor)
    return render(request, 'TailorApp/services.html', {'tailor': tailor, 'services': services})


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

    return render(request, 'TailorApp/service_form.html', {'form': form, 'tailor': tailor})


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

    return render(request, 'TailorApp/service_form.html', {'form': form, 'tailor': tailor, 'service': service})


@login_required
def service_delete(request, service_id):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    service = get_object_or_404(Service, id=service_id, tailor=tailor)

    if request.method == 'POST':
        service.delete()
        return redirect('TailorApp:services')

    return render(request, 'TailorApp/service_confirm_delete.html', {'service': service, 'tailor': tailor})


@login_required
def portfolio_list(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    portfolios = Portfolio.objects.filter(tailor=tailor).order_by('-created_at')

    return render(request, 'TailorApp/portfolio.html', {'tailor': tailor, 'portfolios': portfolios})


@login_required
def portfolio_create(request):
    tailor = get_object_or_404(TailorProfile, user=request.user)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)

        if form.is_valid():
            portfolio_item = form.save(commit=False)
            portfolio_item.tailor = tailor
            portfolio_item.save()
            return redirect('TailorApp:portfolio')

    else:
        form = PortfolioForm()

    return render(request, 'TailorApp/portfolio_form.html', {'form': form, 'tailor': tailor})


@login_required
def portfolio_update(request, pk):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    portfolio_item = get_object_or_404(Portfolio, pk=pk, tailor=tailor)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio_item)

        if form.is_valid():
            form.save()
            return redirect('TailorApp:portfolio')

    else:
        form = PortfolioForm(instance=portfolio_item)

    return render(request, 'TailorApp/portfolio_form.html', {'form': form, 'tailor': tailor, 'portfolio': portfolio_item})


@login_required
def portfolio_delete(request, pk):
    tailor = get_object_or_404(TailorProfile, user=request.user)
    portfolio_item = get_object_or_404(Portfolio, pk=pk, tailor=tailor)

    if request.method == 'POST':
        portfolio_item.delete()
        return redirect('TailorApp:portfolio')

    return render(request, 'TailorApp/portfolio_confirm_delete.html', {'portfolio': portfolio_item, 'tailor': tailor})