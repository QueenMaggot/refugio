# src/proyecto_adopciones/views.py
from django.shortcuts import render
from animales.models import Animal
from refugios.models import Refugio
from adopciones.models import Adopcion

def inicio(request):
    context = {
        'total_animales': Animal.objects.filter(adoptado=False).count(),
        'total_adopciones_aprobadas': Adopcion.objects.filter(estado='aprobada').count(),
        'total_refugios': Refugio.objects.count(),
        'animales_destacados': Animal.objects.filter(adoptado=False)[:3],  # 3 animales no adoptados
        'animales_no_adoptados': Animal.objects.filter(adoptado=False), #Traigo todos los animales no adoptados
    }
    return render(request, 'inicio.html', context)