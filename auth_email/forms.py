from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Auth

class AuthCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Auth
        fields = ('username', 'email')

class AuthChangeForm(UserChangeForm):
    class Meta:
        model = Auth
        fields = ('username', 'email')