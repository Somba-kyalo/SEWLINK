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