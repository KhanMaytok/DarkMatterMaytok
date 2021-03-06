from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
