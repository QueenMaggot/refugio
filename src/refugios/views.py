from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Refugio
from .forms import RefugioForm
# Create your views here.

class RefugioListView(ListView): #Quité permisos de mixins porque no los necesito acá
    model = Refugio
    template_name = 'refugios/refugios_listar.html'
    context_object_name = 'refugios'
    permission_required = 'refugios.view_refugio'

class RefugioCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = Refugio
    template_name = 'refugios/refugio_form.html'
    form_class = RefugioForm
    success_url = '/refugios/listado/'
    permission_required = 'refugios.add_refugio'

class RefugioDetailView(DetailView): #Quito permisos de mixins
    model = Refugio
    template_name = 'refugios/refugio_detail.html'
    form_class = RefugioForm
    context_object_name = 'refugio'
    permission_required = 'refugios.view_refugio'

class RefugioUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Refugio
    form_class = RefugioForm
    template_name = 'refugios/refugio_list.html'
    success_url = '/refugios/listado/'
    permission_required = 'refugios.change_refugio'

class RefugioDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Refugio
    template_name = 'refugios/refugio_confirm_delete.html'
    success_url = '/refugios/listado'
    permission_required = 'refugios.delete_refugio'


