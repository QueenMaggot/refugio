from django.db import models
from refugios.models import Refugio
from datetime import date
# Create your models here.

class Animal(models.Model):
    class Especie(models.TextChoices):
        Felino = 'F', 'Felino'
        Canino = 'C', 'Canino'
        Ave = 'A', 'Ave'
        Roedor = 'R', 'Roedor'
        Pez = 'P', 'Pez'
        OTRO = 'O', 'Otro'

    sexo_choices = [
        ('H' , 'Hembra'),
        ('M', 'Macho'),
    ]

    nombre = models.CharField(max_length=30) # Letras max 30
    especie = models.CharField(max_length=1, choices=Especie.choices, default=Especie.OTRO) # Al agregarle el genero DSP de crear un par de usuarios, ponemos por defecto OTRO
    sexo = models.CharField(max_length=1,choices = sexo_choices, default='H')
    descripcion = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField() # Solo guardamos la fecha models.DateField()
    refugio = models.ForeignKey(Refugio, on_delete=models.CASCADE, related_name='animales')
    adoptado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True) # Campos ocultos que maneja django Cuando agrego nuevo, el django solo agrega la fecha
    modificado = models.DateTimeField(auto_now=True) # Al modificar guardamos la fecha y hs
    foto = models.ImageField(upload_to='animales/', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}, {self.especie},{self.descripcion},{self.sexo}, {self.foto}, {self.refugio}'
    
    class Meta: # Para ordenar la info 
        ordering = ['nombre']

    @property
    def edad(self):
        hoy = date.today() #Guardadmos la fecha actual

        anios = hoy.year - self.fecha_nacimiento.year
        meses = hoy.month - self.fecha_nacimiento.month

        if hoy.day < self.fecha_nacimiento.day:
            meses-=1
        
        if meses < 0:
            anios -= 1
            meses += 12

        if anios < 1:
            return f"{meses} Meses"
        return f"{anios} Años"

        #return hoy.year - self.fecha_nacimiento.year - ( # año actual - nac del animal MENOS 0 o 1 (si cumplio años o no)
        #    (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day) #compara mes y dia para ver si cumplio años o no, devuelve 0 o 1 y se resta
        #)
    

