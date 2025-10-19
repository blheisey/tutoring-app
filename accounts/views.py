# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, EditHoursForm
from .models import TA as CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class EditHoursView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = EditHoursForm
    template_name = "accounts/add_hours.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        # Only allow the logged-in user to edit their own info
        return self.request.user

class TAListView(ListView):
    model = CustomUser
    template_name = "home.html"
    context_object_name = "tas"

class TADetailView(DetailView):
    model = CustomUser
    template_name = "accounts/ta_detail.html"
    context_object_name = "ta"