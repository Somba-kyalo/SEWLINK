from django.db import models
from django.contrib.auth.models import User

from CustomerApp.models import CustomerProfile
from TailorApp.models import TailorProfile

class Conversation(models.Model):


customer = models.ForeignKey(
    CustomerProfile,
    on_delete=models.CASCADE,
    related_name='conversations'
)

tailor = models.ForeignKey(
    TailorProfile,
    on_delete=models.CASCADE,
    related_name='conversations'
)

created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['-updated_at']
    constraints = [
        models.UniqueConstraint(
            fields=['customer', 'tailor'],
            name='unique_customer_tailor_conversation'
        )
    ]

def __str__(self):
    return f"{self.customer} - {self.tailor}"


class Message(models.Model):


conversation = models.ForeignKey(
    Conversation,
    on_delete=models.CASCADE,
    related_name='messages'
)

sender = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='sent_messages'
)

content = models.TextField()

is_read = models.BooleanField(default=False)

created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['created_at']

def __str__(self):
    return f"{self.sender.username}: {self.content[:30]}"

