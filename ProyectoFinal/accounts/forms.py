from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User                                               #agregamos los campos
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Usuario', 'email':'correo'}
        help_texts= {k:"" for k in fields}
        
###
class UserEditForm(UserCreationForm):
    #Aca se define lo que se quiere editar
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contrasena', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model= models.Avatar
        fields=['imagen']