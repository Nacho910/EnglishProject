from django import forms
from django.contrib.auth.forms import UserCreationForm
from django .forms import ModelForm, TextInput, NumberInput, Select, DateInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from .models import Profesor, Comentario, Curso


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'apellido', 'edad', 'email', 'fecha_nacimiento')
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'control',
                'placeholder': 'Nombre Profesor',
                'style': 'max-width: 300px;',
                'label': 'nombre',
                'required': 'True',
                'max_length': '50',
                }),
            'apellido': forms.TextInput(attrs={
                'class': 'control',
                'placeholder': 'apellido',
                'style': 'max-width: 300px;',
                'label': 'Apellido Profesor',
                'required': 'True',
                'max_length': '50'
                }),
            'edad': forms.NumberInput(attrs={
                'class': 'control',
                'placeholder': 'edad',
                'style': 'max-width: 300px;',
                'label': 'Edad Profesor',
                'required': 'True',
                'max_length': '50'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'control',
                'placeholder': 'email',
                'style': 'max-width: 300px;',
                'label': 'Correo Electrónico',
                'required': 'True',
                'max_length': '50'
                }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'control',
                'placeholder': 'fecha_nacimiento',
                'style': 'max-width: 300px;',
                'label': 'Fecha de Nacimiento',
                'required': 'True',
                'max_length': '50'
                })
        }
      

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'control', 'placeholder': 'Contraseña', 'style': 'max-width: 300px;', 'label': 'Contraseña', 'required': 'True', 'max_length': '50'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'control', 'placeholder': 'Confirmar Contraseña', 'style': 'max-width: 300px;', 'label': 'Confirmar Contraseña', 'required': 'True', 'max_length': '50'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_text = {k:"" for k in fields}


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'comentario')
        widgets = {
            'comentario': forms.TextInput(attrs={
                'class': 'control',
                'placeholder': 'Comentario',
                'style': 'max-width: 300px;',
                'label': 'Comentario',
                'required': 'True',
                'max_length': '500',
                })
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion', 'fecha_inicio', 'duracion', 'precio', 'profesor')
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'control',
                'placeholder': 'Nombre Curso',
                'style': 'max-width: 300px;',
                'label': 'nombre',
                'required': 'True',
                'max_length': '50',
                }),
            'descripcion': forms.TextInput(attrs={
                'class': 'control',
                'placeholder': 'Descripción',
                'style': 'max-width: 300px;',
                'label': 'Descripción',
                'required': 'True',
                'max_length': '500',
                }),
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'control',
                'placeholder': 'Fecha de Inicio',
                'style': 'max-width: 300px;',
                'label': 'Fecha de Inicio',
                'required': 'True',
                'max_length': '50'
                }),
            'duracion': forms.NumberInput(attrs={
                'class': 'control',
                'placeholder': 'Duración',
                'style': 'max-width: 300px;',
                'label': 'Duración',
                'required': 'True',
                'max_length': '50'
                }),
            'precio': forms.NumberInput(attrs={
                'class': 'control',
                'placeholder': 'Precio',
                'style': 'max-width: 300px;',
                'label': 'Precio',
                'required': 'True',
                'max_length': '50'
                }),
            'profesor': forms.Select(attrs={
                'class': 'control'
                }),
        }