from django.contrib.auth.models import AbstractUser
from django.db import models

class TA(AbstractUser):
    day = models.CharField(
        max_length=50,
        blank=True,
        help_text="Example: Monday, Wednesday, Friday"
    )
    hours = models.CharField(
        max_length=50,
        blank=True,
        help_text="Example: 2–4 PM"
    )