from django.urls import path
from .views import RefugioCreateView, RefugioDeleteView, RefugioDetailView, RefugioListView, RefugioUpdateView

app_name = 'refugios'

urlpatterns = [
    path('listado/', RefugioListView.as_view(), name='refugio_list'),
    path('crear/', RefugioCreateView.as_view(), name='refugio_create'),
    path('detalle/<int:pk>/', RefugioDetailView.as_view(), name='refugio_detail'),
    path('actualizar/<int:pk>/', RefugioUpdateView.as_view(), name='refugio_update'),
    path('eliminar/<int:pk>/', RefugioDeleteView.as_view(), name='refugio_delete')
]
