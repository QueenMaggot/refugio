from django.db import models

# Create your models here.

class Refugio(models.Model):
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']