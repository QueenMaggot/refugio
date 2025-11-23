from django.shortcuts import render
from rest_framework import generics
from .serializers import AnimalSerializer
from animales.models import Animal

# Create your views here.

class AnimalListAPIView(generics.ListAPIView):
    queryset = Animal.objects.all() # EJEMPLO : Animal.objects.filter(activo=True)
    serializer_class = AnimalSerializer
    #permission_classes = [] # Permitir acceso publico
