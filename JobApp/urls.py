from django.urls import path
from . import views

app_name = 'JobApp'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('create/', views.job_create, name='job_create'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('<int:pk>/edit/', views.job_update, name='job_update'),
    path('<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('tailor/jobs/', views.tailor_job_list, name='tailor_job_list'),
    path('tailor/jobs/<int:pk>/', views.tailor_job_detail, name='tailor_job_detail'),
    path('tailor/jobs/<int:pk>/accept/', views.accept_job, name='accept_job'),
    path('tailor/jobs/<int:pk>/reject/', views.reject_job, name='reject_job'),
]