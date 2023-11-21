from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import AdvUser


class RegisterForm(UserCreationForm):
    is_treatment = forms.BooleanField(required=True, widget=forms.CheckboxInput, label="Обрабатывать персональные данные")

    class Meta:
        model = AdvUser
        fields = ('first_name', 'username', 'email', 'password1', 'password2', 'is_treatment')
