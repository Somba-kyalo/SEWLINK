from django.db import models

from CustomerApp.models import CustomerProfile


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
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,
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

    deadline = models.DateField(
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