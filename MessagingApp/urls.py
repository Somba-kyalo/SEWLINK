from django.urls import path

from . import views

app_name = 'MessagingApp'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('conversation/<int:conversation_id>/', views.conversation, name='conversation'),
    path('conversation/<int:conversation_id>/send/', views.send_message, name='send_message'),
    path('start/<int:tailor_id>/', views.start_conversation, name='start_conversation'),
]