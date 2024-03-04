from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Kniha
from django import forms
from django.forms.widgets import TextInput, PasswordInput

class RegistracniFormular(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginFormular(AuthenticationForm):
    username = forms.CharField(widget=TextInput(), label="Přihlašovací jméno:")
    password = forms.CharField(widget=PasswordInput(), label="Heslo:")

class PridatKnihuFormular(forms.ModelForm):
    class Meta:
        model = Kniha
        fields = ['nazev_knihy', 'autor', 'zanr', 'pocet_stran', 'rok_vydani', 'obrazek']

class UpravitKnihuFormular(forms.ModelForm):
    class Meta:
        model = Kniha
        fields = ['nazev_knihy', 'autor', 'zanr', 'pocet_stran', 'rok_vydani', 'obrazek']
    