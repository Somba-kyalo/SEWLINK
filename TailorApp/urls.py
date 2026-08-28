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

    path('orders/', views.order_list, name='orders'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/confirm/', views.confirm_order, name='confirm_order'),
    path('orders/<int:pk>/start/', views.start_order, name='start_order'),
    path('orders/<int:pk>/complete/', views.complete_order, name='complete_order'),
]