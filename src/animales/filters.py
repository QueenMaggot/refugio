# animales/filters.py
import django_filters
from .models import Animal
from django import forms
from datetime import date
from dateutil.relativedelta import relativedelta

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

        # Filtro por etapa de vida
    ETAPAS = (
        ('bebe', 'Bebé (0 - 6 meses)'),
        ('joven', 'Joven (6 meses - 2 años)'),
        ('adulto', 'Adulto (2 - 7 años)'),
        ('adulto mayor', 'Adulto mayor (7+ años)'),
        ('anciano', 'Anciano (10+ años)'),
    )
    
    etapa = django_filters.ChoiceFilter(
        choices=ETAPAS,
        method='filtrar_por_etapa',
        label='Edad',
        empty_label="Todas las edades"
    )

    class Meta:
        model = Animal
        fields = ['especie','sexo','adoptado']

    def filtrar_por_etapa(self, queryset, name, value):
        if not value:
            return queryset

        hoy = date.today()

        if value == 'bebe':
            # Nacidos en los últimos 6 meses
            fecha_inicio = hoy - relativedelta(months=6)
            return queryset.filter(fecha_nacimiento__gte=fecha_inicio)

        elif value == 'joven':
        # Entre 6 meses y 2 años
            fecha_inicio = hoy - relativedelta(years=2)
            fecha_fin = hoy - relativedelta(months=6)
            return queryset.filter(
                fecha_nacimiento__gte=fecha_inicio,
                fecha_nacimiento__lte=fecha_fin
            )

        elif value == 'adulto':
            # Entre 2 y 7 años
            fecha_inicio = hoy - relativedelta(years=7)
            fecha_fin = hoy - relativedelta(years=2)
            return queryset.filter(
                fecha_nacimiento__gte=fecha_inicio,
                fecha_nacimiento__lte=fecha_fin
            )

        elif value == 'adulto mayor':
            # > 7  años
            fecha_limite = hoy - relativedelta(years=7)
            return queryset.filter(fecha_nacimiento__lte=fecha_limite)
        
        elif value == 'anciano':
        #  > 10 años
            fecha_limite = hoy - relativedelta(years=10)
            return queryset.filter(fecha_nacimiento__lte=fecha_limite)


        return queryset