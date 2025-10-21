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
        fields = ["days", "hours", "information"]
        labels = {
            "information": "What classes are you interested in tutoring?",
        }
        help_texts = {
            "days": None,   # disable default help text
            "hours": None,
            "information": None,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Replace help texts with placeholders
        self.fields['days'].widget.attrs.update({
            'placeholder': 'Enter available days (e.g. Mon, Wed, Fri)',
            'class': 'form-control',  # optional: Bootstrap styling
        })
        self.fields['hours'].widget.attrs.update({
            'placeholder': 'Enter your available hours (e.g. 9am–1pm)',
            'class': 'form-control',
        })
