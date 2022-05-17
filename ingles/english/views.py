from multiprocessing import context
from ssl import AlertDescription
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout



from .models import Profesor, Comentario
from .forms import ProfesorForm, UserRegistrationForm, ComentarioForm
# Create your views here.

def index(request):
    return render(request, 'ruta/index.html')


def formulario(request):
    return render(request, 'ruta/formulario.html')

def registro(request):
    return render(request, 'ruta/registro.html')

def comentario(request):
    form = ComentarioForm(request.POST or None)
    form_class = ComentarioForm
    if request.method == 'POST':
            
            form = ComentarioForm(request.POST)
    
            if form.is_valid():
                #print('Formulario valido')
                comentario = Comentario()
                comentario.nombre = form.cleaned_data['nombre']
                comentario.comentario = form.cleaned_data['comentario']
                comentario.save()
                messages.success(request, f'Comentario creado exitosamente.')
                return redirect('index')

            else:
                print('Formulario invalido')
    return render(request, 'ruta/comentario.html', {'form': form})
    



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
            return redirect('valido')
            
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

def registro(request):
    if request.method == 'POST':    
        form = UserCreationForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Cuenta {username} creada exitosamente.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}

    return render(request, 'ruta/registro.html', context)

