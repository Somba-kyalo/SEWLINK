from django.db import models

from CustomerApp.models import CustomerProfile
from TailorApp.models import TailorProfile, Service


class Job(models.Model):

    CATEGORY_CHOICES = [
        ('tailoring', 'Tailoring'),
        ('alteration', 'Clothing Alteration'),
        ('repair', 'Clothing Repair'),
        ('embroidery', 'Embroidery'),
        ('design', 'Clothing Design'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    tailor = models.ForeignKey(
        TailorProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='jobs'
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='jobs'
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='tailoring'
    )

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    agreed_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    deadline = models.DateField(
        null=True,
        blank=True
    )

    requested_date = models.DateField(
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=150
    )

    reference_image = models.ImageField(
        upload_to='job_references/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title