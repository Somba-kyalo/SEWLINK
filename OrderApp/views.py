from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from CustomerApp.models import CustomerProfile
from TailorApp.models import TailorProfile
from .models import Order


@login_required
def order_list(request):
    customer = get_object_or_404(CustomerProfile, user=request.user)

    orders = Order.objects.filter(
        customer=customer
    ).select_related(
        'job',
        'tailor'
    ).order_by('-created_at')

    return render(request, 'OrderApp/order_list.html', {
        'customer': customer,
        'orders': orders,
    })


@login_required
def order_detail(request, pk):
    customer = get_object_or_404(CustomerProfile, user=request.user)

    order = get_object_or_404(
        Order.objects.select_related('job', 'tailor', 'customer'),
        pk=pk,
        customer=customer
    )

    return render(request, 'OrderApp/order_detail.html', {
        'order': order,
        'customer': customer,
    })


@login_required
def order_tracking(request, pk):
    customer = get_object_or_404(CustomerProfile, user=request.user)

    order = get_object_or_404(
        Order.objects.select_related('job', 'tailor', 'customer'),
        pk=pk,
        customer=customer
    )

    return render(request, 'OrderApp/order_tracking.html', {
        'order': order,
        'customer': customer,
    })