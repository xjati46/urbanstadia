from django.urls import path
from .views import *


app_name = 'main-app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profil/', UserProfileView.as_view(), name='profile'),
    path('profil/create/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profil/<int:pk>/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('cabor/', CaborListView.as_view(), name='cabor'),
    path('cabor/<int:pk>/', CaborDetailView.as_view(), name='cabor-detail'),
    path('pertandingan/create/', PertandinganCreateView.as_view(), name='pertandingan-create'),
    path('pertandingan/<int:pk>/', PertandinganDetailView.as_view(), name='pertandingan-detail'),
    path('pertandingan/<int:pk>/daftar/', DaftarPertandinganCreateView.as_view(), name='daftarpertandingan-create'),
]
