from django import forms
from .models import *


class Shaxsiy_kabinetForm(forms.ModelForm):
    class Meta:
        model = Shaxsiy_kabinet
        fields = "__all__"


class BolimForm(forms.ModelForm):
    class Meta:
        model = Bolim
        fields = "__all__"
