from tkinter import Widget
from django.db import models
import datetime

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(max_length=254, verbose_name='Correo electrónico')
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    
    

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    def corregir_nombre(self):
        return self.nombre.upper()


class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.TextField(max_length=500)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha_inicio = models.DateField(default=datetime.date.today)
    duracion = models.IntegerField()
    precio = models.FloatField()
    profesor = models.ManyToManyField(Profesor, related_name='cursos')

    def __str__(self):
        return self.nombre