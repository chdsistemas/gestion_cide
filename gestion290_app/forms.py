from django import forms
from gestion290_app.models import *
from django.core.exceptions import ValidationError



class FormularioRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['codigo', 'nombre', 'descripcion']




class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'tipo_doc',
            'numero_doc',
            'username',
            'first_name', 
            'last_name',
            'telefono',
            'email',
            'password',
            'rol'
            ]
        widgets = {
            'password': forms.PasswordInput()
        }


