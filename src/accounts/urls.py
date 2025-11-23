# accounts/urls.py

from django.urls import path
from .import views

urlpatterns = [
    path('registro/', views.registro_adoptante, name='registro_adoptante'),
]