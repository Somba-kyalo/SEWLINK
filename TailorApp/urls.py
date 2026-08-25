from django.urls import path
from . import views

app_name = 'TailorApp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]