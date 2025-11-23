from django.db import models
from animales.models import Animal
from adoptantes.models import Adoptante

# Create your models here.

class Adopcion(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE, related_name='adopciones')
    fecha_adopcion = models.DateField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')])

    def __str__(self):
        return f'{self.animal}, {self.adoptante}' #
    
    #class Meta: # Para ordenar la info 
     #   constraints = [ #Para que cada adoptante tenga un solo pendiente, no pueda pedir + de 1 animal hasta que no ACEPTEN/RECHACEN
      #      models.UniqueConstraint(
       #         fields=['adoptante'],
        #        condition=models.Q(estado='pendiente'),
         #       name='unique_adoptante_pendiente'
          #  )
        #]