# animales/filters.py
import django_filters
from .models import Animal
from django import forms

class AnimalFilter(django_filters.FilterSet):
    especie = django_filters.ChoiceFilter(
        choices=Animal.Especie.choices,
        empty_label="Todas las especies"
    )
    sexo = django_filters.MultipleChoiceFilter(
        choices=Animal.sexo_choices,
        widget = forms.CheckboxSelectMultiple
        
    )
    adoptado = django_filters.BooleanFilter(
        label="¿Adoptado?",
        widget=django_filters.widgets.BooleanWidget
    )

    class Meta:
        model = Animal
        fields = ['especie','sexo','adoptado']