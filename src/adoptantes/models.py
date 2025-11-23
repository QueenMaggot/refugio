from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Adoptante(models.Model):
    class Genero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMENINO = 'F', 'Femenino'
        OTRO = 'O', 'Otro'
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30) # Letras max 30
    genero = models.CharField(max_length=1, choices=Genero.choices, default=Genero.OTRO) # Al agregarle el genero DSP de crear un par de usuarios, ponemos por defecto OTRO
    dni = models.BigIntegerField() # Un entero grande
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #El user de las cuentas va a ser un adoptante.
    fecha_nacimiento = models.DateField() # Solo guardamos la fecha
    email = models.EmailField() # Campo TIPO EMAIL, no requerido
    domicilio = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True) # Campos ocultos que maneja django Cuando agrego nuevo, el django solo agrega la fecha
    modificado = models.DateTimeField(auto_now=True) # Al modificar guardamos la fecha y hs

    def __str__(self):
        return f'{self.apellido}, {self.nombre}' 
    
    class Meta: # Para ordenar la info 
        ordering = ['apellido', 'nombre']

    @property
    def edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
