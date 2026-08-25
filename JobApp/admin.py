from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'customer',
        'category',
        'budget',
        'deadline',
        'status',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'customer__full_name',
        'customer__phone',
    )

    list_filter = (
        'category',
        'status',
        'created_at',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )