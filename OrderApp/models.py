from django.db import models

from CustomerApp.models import CustomerProfile
from TailorApp.models import TailorProfile
from JobApp.models import Job


class Order(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    job = models.OneToOneField(
        Job,
        on_delete=models.CASCADE,
        related_name='order'
    )

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    tailor = models.ForeignKey(
        TailorProfile,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    agreed_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Order #{self.id} - {self.job.title}"