from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'job',
        'customer',
        'tailor',
        'agreed_price',
        'status',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'job__title',
        'customer__full_name',
        'tailor__full_name',
        'tailor__business_name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )