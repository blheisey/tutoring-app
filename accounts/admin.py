# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import TA

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = TA
    list_display = [
        "email",
        "username",
        "day",
        "hours",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("day", "hours")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("day", "hours")}),)


admin.site.register(TA, CustomUserAdmin)