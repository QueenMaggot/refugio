from django.urls import path
from .views import AnimalCreateView, AnimalUpdateView, AnimalListView, AnimalDeleteView, AnimalDetailView

app_name = 'animales'

urlpatterns = [
    path('listado/', AnimalListView.as_view(), name = 'animal_list'),
    path('crear/', AnimalCreateView.as_view(), name='animal_create'),
    path('detalle/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
    path('actualizar/<int:pk>/', AnimalUpdateView.as_view(), name='animal_update'),
    path('eliminar/<int:pk>/', AnimalDeleteView.as_view(), name='animal_delete')
]

