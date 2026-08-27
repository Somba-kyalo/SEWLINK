from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from CustomerApp.models import CustomerProfile
from TailorApp.models import TailorProfile

from .models import Conversation, Message


@login_required
def inbox(request):
    customer = CustomerProfile.objects.filter(user=request.user).first()
    tailor = TailorProfile.objects.filter(user=request.user).first()

    conversations = Conversation.objects.none()

    if customer:
        conversations = Conversation.objects.filter(
            customer=customer
        ).select_related(
            'customer',
            'tailor',
            'tailor__user'
        ).prefetch_related(
            'messages'
        ).annotate(
            unread_count=Count(
                'messages',
                filter=~Q(messages__sender=request.user) & Q(messages__is_read=False)
            )
        ).order_by('-updated_at')

    elif tailor:
        conversations = Conversation.objects.filter(
            tailor=tailor
        ).select_related(
            'customer',
            'customer__user',
            'tailor'
        ).prefetch_related(
            'messages'
        ).annotate(
            unread_count=Count(
                'messages',
                filter=~Q(messages__sender=request.user) & Q(messages__is_read=False)
            )
        ).order_by('-updated_at')

    for conversation_item in conversations:
        conversation_item.last_message = conversation_item.messages.order_by('-created_at').first()

    return render(
        request,
        'MessagingApp/inbox.html',
        {'conversations': conversations}
    )


@login_required
def conversation(request, conversation_id):
    conversation_item = get_object_or_404(
        Conversation.objects.select_related(
            'customer',
            'customer__user',
            'tailor',
            'tailor__user'
        ),
        id=conversation_id
    )

    customer = CustomerProfile.objects.filter(user=request.user).first()
    tailor = TailorProfile.objects.filter(user=request.user).first()

    if not (
        (customer and conversation_item.customer == customer)
        or
        (tailor and conversation_item.tailor == tailor)
    ):
        return redirect('MessagingApp:inbox')

    messages = conversation_item.messages.select_related(
        'sender'
    ).order_by('created_at')

    messages.filter(
        is_read=False
    ).exclude(
        sender=request.user
    ).update(
        is_read=True
    )

    if customer and conversation_item.customer == customer:
        recipient = conversation_item.tailor.user
        recipient_name = conversation_item.tailor.full_name
    else:
        recipient = conversation_item.customer.user
        recipient_name = conversation_item.customer.full_name

    return render(
        request,
        'MessagingApp/conversation.html',
        {
            'conversation': conversation_item,
            'messages': messages,
            'recipient': recipient,
            'recipient_name': recipient_name,
        }
    )


@login_required
def send_message(request, conversation_id):
    conversation_item = get_object_or_404(
        Conversation,
        id=conversation_id
    )

    customer = CustomerProfile.objects.filter(user=request.user).first()
    tailor = TailorProfile.objects.filter(user=request.user).first()

    if not (
        (customer and conversation_item.customer == customer)
        or
        (tailor and conversation_item.tailor == tailor)
    ):
        return redirect('MessagingApp:inbox')

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()

        if content:
            Message.objects.create(
                conversation=conversation_item,
                sender=request.user,
                content=content
            )

            conversation_item.save(update_fields=['updated_at'])

    return redirect(
        'MessagingApp:conversation',
        conversation_id=conversation_item.id
    )


@login_required
def start_conversation(request, tailor_id):
    customer = get_object_or_404(
        CustomerProfile,
        user=request.user
    )

    tailor = get_object_or_404(
        TailorProfile,
        id=tailor_id
    )

    conversation_item, created = Conversation.objects.get_or_create(
        customer=customer,
        tailor=tailor
    )

    return redirect(
        'MessagingApp:conversation',
        conversation_id=conversation_item.id
    )