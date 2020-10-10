from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(CabangOlahraga)
class CabangOlahragaAdmin(admin.ModelAdmin):
    pass


@admin.register(KelasPertandingan)
class KelasPertandinganAdmin(admin.ModelAdmin):
    pass


@admin.register(Pertandingan)
class PertandinganAdmin(admin.ModelAdmin):
    pass


@admin.register(PesertaPertandingan)
class PesertaPertandinganAdmin(admin.ModelAdmin):
    pass
