# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TA as CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("days", "hours", "first_name", "last_name", "information")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields