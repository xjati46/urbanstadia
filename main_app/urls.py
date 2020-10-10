from django.urls import path
from .views import *


app_name = 'main-app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profil/', UserProfileView.as_view(), name='profile'),
    path('profil/create/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profil/<int:pk>/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('pertandingan/', PertandinganListView.as_view(), name='pertandingan'),
    path('pertandingan/create/', PertandinganCreateView.as_view(), name='pertandingan-create'),
]
