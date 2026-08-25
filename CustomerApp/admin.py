from django.contrib import admin

from .models import CustomerProfile


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'user',
        'phone',
        'location',
        'created_at',
    )

    search_fields = (
        'full_name',
        'phone',
        'location',
        'user__username',
        'user__email',
    )

    list_filter = (
        'location',
        'created_at',
    )