# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from adoptantes.models import Adoptante

class RegistroAdoptanteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Adoptante
        fields = ['dni', 'nombre', 'apellido', 'fecha_nacimiento', 'domicilio', 'telefono', 'genero']
    
    def clean_dni(self):
        #validamos que el dni sea unico
        dni = self.cleaned_data['dni']
        if User.objects.filter(username=str(dni)).exists():
            raise forms.ValidationError('Este DNI ya se encuentra registrado.')
        if Adoptante.objects.filter(dni=dni).exists():
            raise forms.ValidationError('Este DNI ya se encuentras registrado.')
        return dni

    def save(self, commit=True):
        # Crea el usuario
        user = User.objects.create_user(
            username=self.cleaned_data['dni'],
            password=self.cleaned_data['password'],
            first_name = self.cleaned_data['nombre'],
            last_name = self.cleaned_data['apellido'],
            email = self.cleaned_data['email']
        )
        # Crea el adoptante vinculado
        adoptante = super().save(commit=False)
        adoptante.user = user
        if commit:
            adoptante.save()
        return adoptante