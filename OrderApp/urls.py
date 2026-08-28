from django.urls import path
from . import views


app_name = 'OrderApp'


urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('<int:pk>/tracking/', views.order_tracking, name='order_tracking'),
]