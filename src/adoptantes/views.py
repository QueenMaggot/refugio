from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Adoptante
from .forms import AdoptanteForm
# Create your views here.

class AdoptanteListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = Adoptante
    template_name = 'adoptantes/adoptantes_listar.html'
    context_object_name = 'adoptantes'
    permission_required = 'adoptantes.view_animal'

class AdoptanteCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = Adoptante
    form_class= AdoptanteForm
    template_name = 'adoptantes/adoptante_form.html'
    success_url = '/adoptantes/listado/'
    permission_required = 'adoptantes.add_adoptante'

class AdoptanteDetailView(PermissionRequiredMixin,LoginRequiredMixin, DetailView):
    model = Adoptante
    template_name = 'adoptantes/adoptante_detail.html'
    context_object_name = 'adoptante'
    permission_required = 'adoptantes.view_adoptante'

class AdoptanteUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Adoptante
    form_class= AdoptanteForm
    template_name = 'adoptantes/adoptante_list.html'
    success_url = '/adoptantes/listado/'
    permission_required = 'adoptantes.change_adoptante'

class AdoptanteDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Adoptante
    template_name = 'adoptantes/adoptante_confirm_delete.html'
    success_url = '/adoptantes/listado'
    permission_required = 'adoptantes.delete_adoptante'


