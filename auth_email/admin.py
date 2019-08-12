from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AuthCreationForm, AuthChangeForm
from .models import Auth

class AuthAdmin(UserAdmin):
    add_form = AuthCreationForm
    form = AuthChangeForm
    model = Auth
    list_display = ['email', 'username',]

admin.site.register(Auth, AuthAdmin)