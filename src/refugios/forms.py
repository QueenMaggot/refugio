from django import forms
from .models import Refugio

class RefugioForm(forms.ModelForm):
    class Meta:
        model = Refugio
        fields = ['nombre', 'domicilio', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }