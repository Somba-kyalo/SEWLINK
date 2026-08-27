from django.contrib import admin

from .models import Conversation, Message


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):

    list_display = (
        'customer',
        'tailor',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'customer__full_name',
        'tailor__full_name',
    )

    list_filter = (
        'created_at',
        'updated_at',
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'conversation',
        'sender',
        'is_read',
        'created_at',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

    search_fields = (
        'sender__username',
        'content',
    )