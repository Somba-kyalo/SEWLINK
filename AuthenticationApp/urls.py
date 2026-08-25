from django.urls import path

from . import views


app_name = 'AuthenticationApp'


urlpatterns = [
    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'dashboard/',
        views.dashboard_redirect,
        name='dashboard_redirect'
    ),
]