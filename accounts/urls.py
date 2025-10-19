# accounts/urls.py
from django.urls import path
from .views import SignUpView,  EditHoursView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("add-hours/", EditHoursView.as_view(), name="add_hours"),

]