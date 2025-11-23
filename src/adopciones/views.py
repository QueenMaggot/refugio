

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Adopcion, Animal
from .forms import AdopcionForm, AdopcionEdicionForm
from datetime import date
# Create your views here.

class AdopcionListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = Adopcion
    template_name = 'adopciones/adopciones_listar.html'
    context_object_name = 'adopciones'
    permission_required = 'adopciones.view_adopcion'

class AdopcionCreateView(LoginRequiredMixin, CreateView): #Solo necesito el permiso del LOGIN
    model = Adopcion
    form_class = AdopcionForm
    template_name = 'adopciones/adopcion_form.html'
    success_url = reverse_lazy('animales:animal_list')
    #permission_required = 'adopciones.add_adopcion' CREO QUE ESTE PERMISO NO VA

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['adoptante'] = self.request.user.adoptante  # ← Pasamos el adoptante
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        animal_id = self.kwargs.get('animal_id')
        if animal_id:
            initial['animal'] = animal_id
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animal']  =get_object_or_404(Animal, id=self.kwargs['animal_id'])
        context['today'] = date.today()
        #animal_id = self.kwargs.get('animal_id')
        #if animal_id:
        #    context['animal'] = get_object_or_404(Animal, id=animal_id)
        return context

    def form_valid(self, form):
        #Asignar adoptante actual
        form.instance.adoptante = self.request.user.adoptante
        # Siempre arranca como pendiente (despues un admin la aprueba o rechaza)
        form.instance.animal = get_object_or_404(Animal, id=self.kwargs['animal_id'])
        form.instance.estado = 'pendiente'
        form.instance.fecha_adopcion = date.today() #fecha automatica (HOY)
        
            # ¡Importante! El campo 'animal' está disabled → no viene en form.cleaned_data
            # Así que lo tomamos de la URL:
        animal_id  =self.kwargs.get('animal_id')
        form.instance.animal = get_object_or_404(Animal, id=animal_id)

        response = super().form_valid(form)
            # Mensaje de éxito personalizado

        messages.success(
            self.request,
            f"¡Solicitud de adopción enviada para {self.object.animal.nombre} "
            f"({self.object.animal.get_sexo_display()}, "
            f"{self.object.animal.get_especie_display()})!"
        )
        return response

class AdopcionDetailView(PermissionRequiredMixin,LoginRequiredMixin, DetailView):
    model = Adopcion
    template_name = 'adopciones/adopcion_detail.html'
    context_object_name = 'adopcion'
    permission_required = 'adopciones.view_adopcion'

class AdopcionUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Adopcion
    form_class = AdopcionEdicionForm
    template_name = 'adopciones/adopcion_list.html'
    success_url = reverse_lazy('adopciones:adopcion_list')
    permission_required = 'adopciones.change_adopcion'
    
    def form_valid(self, form):
        response = super().form_valid(form)
                
        # Solo marca el animal como adoptado si la adopción está APROBADA
        if self.object.estado == 'aprobada':
            self.object.animal.adoptado = True
            self.object.animal.save(update_fields=['adoptado'])
        
        elif self.object.estado != 'aprobada' and self.get_object().estado == 'aprobada':
            self.object.animal.adoptado = False
            self.object.animal.save(update_fields=['adoptado'])

        return response

class AdopcionDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Adopcion
    template_name = 'adopciones/adopcion_confirm_delete.html'
    success_url = '/adopciones/listado'
    permission_required = 'adopciones.delete_adopcion'