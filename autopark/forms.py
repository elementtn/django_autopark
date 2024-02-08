import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Driver, Car, CarBrand, Client
from AutoparkProject.settings import DATE_INPUT_FORMATS

class RegistratinForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ["username", "email"]

        labels = {
            'username': 'Логин',
            'password1': 'пароль',
            'password2': 'пароль еще раз'
        }
        help_texts = {
            "username": '',
            "password1": '',

        }

class DriverForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y'), input_formats=('%d.%m.%Y'))
    class Meta:
        model = Driver
        exclude = ["user", "is_available"]
