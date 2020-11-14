from django import forms
from django.forms import ModelForm

from .models import *


class PassForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = '__all__'
