from django.contrib import admin
from .models import Skill, TailorProfile, Service, Portfolio


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(TailorProfile)
class TailorProfileAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'full_name', 'phone', 'location', 'experience_years', 'is_verified', 'is_available', 'created_at')
    search_fields = ('business_name', 'full_name', 'phone', 'location', 'user__username')
    list_filter = ('is_verified', 'is_available', 'location')
    filter_horizontal = ('skills',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'tailor', 'starting_price', 'estimated_days', 'created_at')
    search_fields = ('name', 'tailor__business_name')
    list_filter = ('estimated_days', 'created_at')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'tailor', 'created_at')
    search_fields = ('title', 'tailor__business_name')
    list_filter = ('created_at',)