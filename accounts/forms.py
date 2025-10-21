# accounts/forms.py
# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import TA as CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "days",
            "hours",
            "information",

        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


# ✅ NEW FORM for editing hours/days
class EditHoursForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["days", "hours"]

