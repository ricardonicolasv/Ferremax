from django import forms
from django.contrib.auth.models import User
from .models import Producto, CategoriaProducto, Especialidad


class RegistroForm(forms.Form):
    nombre_completo = forms.CharField(label='Nombre Completo', max_length=100)
    email = forms.EmailField(label='Correo')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirmar_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise forms.ValidationError(
                "Las contraseñas no coinciden."
            )

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_especialidad', 'id_categoria', 'codigo_upc', 'nombre', 'marca']