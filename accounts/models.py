from django.contrib.auth.models import AbstractUser
from django.db import models

class TA(AbstractUser):
    days = models.CharField(
        max_length=50,
        blank=True,
    )
    hours = models.CharField(
        max_length=50,
        blank=True,
    )
    information = models.TextField(blank=True )