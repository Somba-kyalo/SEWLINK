from django.urls import path
from . import views

app_name = 'TailorApp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('services/', views.services, name='services'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:service_id>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:service_id>/delete/', views.service_delete, name='service_delete'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio/create/', views.portfolio_create, name='portfolio_create'),
    path('portfolio/<int:pk>/edit/', views.portfolio_update, name='portfolio_update'),
    path('portfolio/<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),
]