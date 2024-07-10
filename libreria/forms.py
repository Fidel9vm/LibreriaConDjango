from django import forms
from .models import Libro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Letras, números y @/./+/-/_ solamente.',
            'password1': 'La contraseña debe tener al menos 8 caracteres.',
            'password2': 'Introduce la misma contraseña para verificación.',
        }
        error_messages = {
            'username': {
                'required': 'Este campo es obligatorio.',
                'unique': 'Un usuario con ese nombre ya existe.',
            },
        }