from django.urls import path
from .views import AdoptanteCreateView, AdoptanteDeleteView, AdoptanteDetailView, AdoptanteListView, AdoptanteUpdateView

app_name = 'adoptantes'

urlpatterns = [
    path('listado/', AdoptanteListView.as_view(), name = 'adoptante_list'),
    #path('crear/', AdoptanteCreateView.as_view(), name='adoptante_create'),
    path('detalle/<int:pk>/', AdoptanteDetailView.as_view(), name='adoptante_detail'),
    path('actualizar/<int:pk>/', AdoptanteUpdateView.as_view(), name='adoptante_update'),
    path('eliminar/<int:pk>/', AdoptanteDeleteView.as_view(), name='adoptante_delete')
]

