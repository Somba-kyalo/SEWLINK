from django.contrib import admin
from django.urls import include, path

from .views import home


urlpatterns = [
    path('', home, name='home'),

    path('admin/', admin.site.urls),

    path('auth/', include('AuthenticationApp.urls')),
    path('customer/', include('CustomerApp.urls')),
    path('tailor/', include('TailorApp.urls')),
    path('jobs/', include('JobApp.urls')),
    path('adminpanel/', include('AdminApp.urls')),
]