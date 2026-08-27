from django.conf import settings
from django.conf.urls.static import static
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
    path('messages/', include('MessagingApp.urls')),
    path('adminpanel/', include('AdminApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)