from django.contrib.auth.models import AbstractUser
from django.db import models

class TA(AbstractUser):
    days = models.CharField(
        max_length=50,
        blank=True,
        help_text="Example: Mondays, Wednesdays, Fridays"
    )
    hours = models.CharField(
        max_length=50,
        blank=True,
        help_text="Example: 2–4 PM"
    )
    information = models.TextField(blank=True, help_text="Optional: Add info about yourself, including classes you'd be comfortable tutoring.")