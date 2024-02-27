from django import forms
from .models import *


class ShaxsForm(forms.ModelForm):
    class Meta:
        model = Shaxs
        fields = ['ism', 'familiya', 'bolim', 'tel', 'address']


class BolimForm(forms.ModelForm):
    class Meta:
        model = Bolim
        fields = "__all__"


class XabarlarForm(forms.ModelForm):
    class Meta:
        model = Xabarlar
        fields = "__all__"


class ArizaForm(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = "__all__"


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['jonatuvchi', 'oluvchi', 'mavzu', 'tarkib']
