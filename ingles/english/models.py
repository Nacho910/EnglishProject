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