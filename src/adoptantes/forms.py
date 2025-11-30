# adoptantes/forms.py

from django import forms
from .models import Adoptante

class AdoptanteForm(forms.ModelForm):
    email = forms.EmailField(
    label="Email",
    required=False,
    widget=forms.EmailInput(attrs={'class': 'form-control'})
)

    class Meta:
        model = Adoptante
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'dni', 'genero',
                  'telefono', 'domicilio', 'activo']  # quite email

        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d'
            ),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si el adoptante ya tiene user, mostrar su email
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email
    
    # Guardamos email en user asociado
    def save(self, commit=True):
        adoptante = super().save(commit=False)
        email = self.cleaned_data.get('email')
        if adoptante.user and email:
            adoptante.user.email = email
            if commit:
                adoptante.user.save()
        if commit:
            adoptante.save()
        return adoptante
