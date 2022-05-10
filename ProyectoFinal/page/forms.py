from dataclasses import fields
from socket import fromshare
from django import forms 
from . import models 



class CreateArticulo(forms.ModelForm):
    class Meta:
        model=models.articulo
        fields= ['titulo','descripcion','cuerpo','imagen']