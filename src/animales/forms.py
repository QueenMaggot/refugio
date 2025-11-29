from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'especie', 'sexo', 'descripcion', 'fecha_nacimiento', 'refugio', 'foto', 'adoptado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d'  # ← Esto es clave
            ),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'refugio': forms.Select(attrs={'class': 'form-select'}),
            'adoptado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegurar compatibilidad con el formato del navegador
        self.fields['fecha_nacimiento'].input_formats = ['%Y-%m-%d']
        # ¡NO toques initial! Django lo maneja desde la instancia.