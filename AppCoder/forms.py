
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PacienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)  
    documento_pac = forms.IntegerField()

class MedicoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)  
    Profesion = forms.CharField(max_length=30)

class PracticaFormulario(forms.Form):
    practica_nombre= forms.CharField(max_length=30)
    documento_pac = forms.IntegerField()
    fecha_practica= forms.DateField()

class UserEditForm(forms.Form):
     
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label="Confirme cambio con su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

class Meta:
    model = User
    fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
    