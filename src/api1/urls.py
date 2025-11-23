from django.urls import path
from .views import AnimalListAPIView

app_name='api1'

urlpatterns = [
    path('animales/', AnimalListAPIView.as_view(), name='api_animal_list'),
]
