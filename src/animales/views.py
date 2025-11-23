from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin #(es una clase que obliga que este log para acceder a ella)
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Animal
from .filters import AnimalFilter
from .forms import AnimalForm
# Create your views here.

class AnimalListView(ListView): #Quité mixins de autenticación, porque no hacen falta
    model = Animal
    template_name = 'animales/animales_listar.html'
    context_object_name = 'animales'
    paginate_by = 9

    def get_queryset(self):
    # Aplica los filtros
        queryset = Animal.objects.all()
        self.filter = AnimalFilter(self.request.GET, queryset=queryset)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter  # Pasa los filtros al template
        return context

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
