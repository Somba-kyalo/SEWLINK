from django.contrib.auth.models import User
from django.db import models


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer_profile'
    )
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    profile_picture = models.ImageField(
        upload_to='customer_profiles/',
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name