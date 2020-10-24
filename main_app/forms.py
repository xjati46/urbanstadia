from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile, Pertandingan, PesertaPertandingan


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PertandinganForm(forms.ModelForm):
    class Meta:
        model = Pertandingan
        fields = '__all__'


class DaftarPertandinganForm(forms.ModelForm):
    class Meta:
        model = PesertaPertandingan
        fields = '__all__'
