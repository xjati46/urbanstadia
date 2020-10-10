from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
    )
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile, Pertandingan


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'main_app/index.html'


class RegistrationView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main_app/profil.html'


class UserProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = UserProfileForm
    success_url = reverse_lazy('main-app:profile')
    template_name = 'main_app/userprofile_form.html'
    model = UserProfile


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    success_url = reverse_lazy('main-app:profile')
    template_name = 'main_app/userprofile_form.html'
    model = UserProfile


class PertandinganListView(LoginRequiredMixin, ListView):
    template_name = 'main_app/pertandingan_list.html'
    model = Pertandingan
    #
    # def get_queryset(self):
    #     set = []
    #     for i in self.request.user.userprofile.cabor_favorit:
    #         set.append(i.id)
    #     return Pertandingan.objects.filter(cabor__in=set)


class PertandinganCreateView(LoginRequiredMixin, CreateView):
    form_class = PertandinganForm
    success_url = reverse_lazy('main-app:pertandingan')
    template_name = 'main_app/pertandingan_form.html'
    model = Pertandingan
