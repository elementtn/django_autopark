import datetime

from django import forms

from .models import Driver, Car, CarBrand, Client
from AutoparkProject.settings import DATE_INPUT_FORMATS

class DriverModelForm(forms.ModelForm):
    class Meta:
        model = Driver
        exlude = ["is_available"]



