from django.shortcuts import render,redirect
from django_filters.views import FilterView
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin #(es una clase que obliga que este log para acceder a ella)
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Animal
from .filters import AnimalFilter
from .forms import AnimalForm

# Create your views here.

class AnimalListView(FilterView): #Quité mixins de autenticación, porque no hacen falta
    model = Animal
    filterset_class = AnimalFilter
    template_name = 'animales/animales_listar.html'
    context_object_name = 'animales'
    paginate_by = 9

    def get_filterset_kwargs(self, filterset_class):
        kwargs = super().get_filterset_kwargs(filterset_class)
        # Si no hay parámetros GET, aplica "adoptado=False" por defecto
        if not self.request.GET:
            kwargs['data'] = {'adoptado': 'False'}
        else:
            kwargs['data'] = self.request.GET
        return kwargs

    def get_queryset(self):
        # El queryset base: todos los animales
        return Animal.objects.select_related('refugio')

class AnimalCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = Animal
    template_name = 'animales/animal_form.html'
    form_class = AnimalForm
    #fields = ['nombre','especie','descripcion','sexo','foto','fecha_nacimiento','refugio', 'adoptado']
    success_url = '/animales/listado/'
    permission_required = 'animales.add_animal'

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animales/animal_detail.html'
    context_object_name = 'animal'
    permission_required = 'animales.view_animal'

class AnimalUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Animal
    template_name = 'animales/animal_list.html'
    fields = ['nombre','especie','descripcion','refugio','foto','adoptado']
    success_url = '/animales/listado/'
    permission_required = 'animales.change_animal'

class AnimalDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'animales/animal_confirm_delete.html'
    success_url = '/animales/listado'
    permission_required = 'animales.delete_animal'
