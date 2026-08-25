from django.urls import path
from . import views

app_name = 'CustomerApp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('tailors/', views.tailor_search, name='tailor_search'),
]