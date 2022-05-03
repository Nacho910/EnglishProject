from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .models import Profesor
from .forms import ProfesorForm, UserRegistrationForm
# Create your views here.

def index(request):
    return render(request, 'ruta/index.html')


def formulario(request):
    return render(request, 'ruta/formulario.html')


def formulario(request):
    form = ProfesorForm(request.POST or None)
    form_class = ProfesorForm
    if request.method == 'POST':
    
        form = ProfesorForm(request.POST)

        if form.is_valid():
            #print('Formulario valido')
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.edad = form.cleaned_data['edad']
            profesor.email = form.cleaned_data['email']
            profesor.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            profesor.save()   #Guardar en la base de datos
        else:
            print('Formulario invalido')


    return render(request, 'ruta/formulario.html', {'form': form})


def valido(request):
    return render(request, 'ruta/valido.html')

def login(request):
    return render(request, 'ruta/login.html')

def login(request):
    if request.method == 'POST':    
        form = UserRegistrationForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Cuenta {username} creada exitosamente.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}

    return render(request, 'ruta/index.html', context)