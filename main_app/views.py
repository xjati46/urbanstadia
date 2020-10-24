from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
    )
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile, Pertandingan, CabangOlahraga, PesertaPertandingan


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


class CaborListView(LoginRequiredMixin, TemplateView):
    template_name = 'main_app/cabor_list.html'


class CaborDetailView(LoginRequiredMixin, DetailView):
    template_name = 'main_app/cabor_detail.html'
    model = CabangOlahraga

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pertandingan_list'] = Pertandingan.objects.filter(cabor=self.kwargs['pk'])
        return context


class PertandinganCreateView(LoginRequiredMixin, CreateView):
    form_class = PertandinganForm
    success_url = reverse_lazy('main-app:cabor')
    template_name = 'main_app/pertandingan_form.html'
    model = Pertandingan


class PertandinganDetailView(LoginRequiredMixin, DetailView):
    template_name = 'main_app/pertandingan_detail.html'
    model = Pertandingan


class DaftarPertandinganCreateView(LoginRequiredMixin, CreateView):
    form_class = DaftarPertandinganForm
    success_url = reverse_lazy('main-app:cabor')
    template_name = 'main_app/daftarpertandingan_form.html'
    model = PesertaPertandingan
