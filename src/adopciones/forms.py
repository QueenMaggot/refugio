# adopciones/forms.py

from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from animales.models import Animal
from adoptantes.models import Adoptante
from .models import Adopcion


class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = []#['animal']  #Eliminé el campo ADOPTANTE, porque lo traigo automaticamente, lo mismo con 'ESTADO' = 'PENDIENTE'
      #  widgets = {
       #     'animal' : forms.Select(attrs={'class': 'form-control', 'disabled' : 'disabled'}),
            #'adoptante' : forms.Select(attrs={'class': 'form-control'}),
            #'estado' : forms.Select(attrs={'class': 'form-control'}),
            
        #}

    def __init__(self, *args, **kwargs):
        self.adoptante = kwargs.pop('adoptante', None)  # ← Recibimos el adoptante
        #self.animal = kwargs.pop('animal', None) # Pasamos el animal 
        super().__init__(*args, **kwargs)

         # Filtra animales disponibles
        #self.fields['animal'].queryset = Animal.objects.filter(adopcion__isnull=True)
        #self.fields['animal'].label_from_instance = lambda obj: f"{obj.id} - {obj.nombre} ({obj.get_especie_display()}, {obj.get_sexo_display()}) - {obj.refugio.nombre}"

            # Si hay un animal en la URL, preseleccionarlo
        #if not self.initial.get('animal'):
        #    #self.initial['animal'].widget.attrs['readonly'] = 'readonly'
        #self.fields['animal'].widget.attrs['disabled'] = 'disabled'
        
    def clean(self):
        cleaned_data = super().clean()
        if self.adoptante:
            # Verifica si el adoptante ya tiene una adopción pendiente
            #if Adopcion.objects.filter(
            adopcion_pendiente = Adopcion.objects.filter(
                adoptante=self.adoptante,
                estado= 'pendiente'
            
            ).first() #).exists(): #exists solo devuelve true o false; first devuelve el objeto completo o NONE
                
            if adopcion_pendiente:
                raise ValidationError(
                    f"Ya tienes una solicitud de adopción pendiente para el animal "
                    f"| {adopcion_pendiente.animal.nombre} |."
                    "Espera a que sea aprobada o rechazada antes de solicitar otra."
                )
        return cleaned_data
    

class AdopcionEdicionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['estado', 'fecha_adopcion']  # ← Solo estos campos
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_adopcion': forms.DateInput(
                #format='%Y-%m-%d',   # ← formato compatible con <input type="date">
                attrs={'type': 'date', 'class': 'form-control'}

            ),
        }