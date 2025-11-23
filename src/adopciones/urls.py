from django.urls import path
from .views import AdopcionCreateView, AdopcionDeleteView, AdopcionDetailView, AdopcionListView, AdopcionUpdateView

app_name= 'adopciones'

urlpatterns = [
    path('listado/', AdopcionListView.as_view(), name= 'adopcion_list'),
    path('crear/<int:animal_id>/', AdopcionCreateView.as_view(), name='adopcion_create'),
    path('detalle<int:pk>/', AdopcionDetailView.as_view(), name='adopcion_detail'),
    path('actualizar<int:pk>/', AdopcionUpdateView.as_view(), name= 'adopcion_update'),
    path('eliminar<int:pk>/', AdopcionDeleteView.as_view(), name='adopcion_delete')

]
