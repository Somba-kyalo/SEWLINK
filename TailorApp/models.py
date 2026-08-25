from django.contrib.auth.models import User
from django.db import models


class TailorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='tailor_profile'
    )
    business_name = models.CharField(max_length=150)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    profile_picture = models.ImageField(
        upload_to='tailor_profiles/',
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name