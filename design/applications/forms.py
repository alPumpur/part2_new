from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    is_treatment = forms.BooleanField(required=True, widget=forms.CheckboxInput, label="Обрабатывать персональные данные")

    class Meta:
        model = AdvUser
        fields = ('first_name', 'username', 'email', 'password1', 'password2', 'is_treatment')


class CreateApplicationForm(forms.ModelForm):

    def clean(self):
        image = self.cleaned_data.get('image_app')

        if image.size > 2097152:
            raise ValidationError("Прикрепляемая фотография должна быть меньше чем 2МБ")

    class Meta:
        model = Application
        fields = ('name_app', 'desc_app', 'category', 'image_app')
