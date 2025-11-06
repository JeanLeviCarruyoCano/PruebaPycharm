from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView
from .forms import SignUpForm, ProfileForm
from .models import Profile

class SignUpView(FormView):
    template_name = "accounts/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "¡Cuenta creada con éxito! Bienvenid@.")
        return super().form_valid(form)

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = "accounts/profile_detail.html"
    context_object_name = "profile"

    def get_object(self):
        return Profile.objects.select_related("user").get(user=self.request.user)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "accounts/profile_form.html"
    form_class = ProfileForm
    success_url = reverse_lazy("accounts:profile")

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Perfil actualizado.")
        return super().form_valid(form)
