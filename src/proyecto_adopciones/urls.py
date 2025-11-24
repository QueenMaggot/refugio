"""
URL configuration for adopciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1/', include ('api1.urls', namespace='api1')),
    path('', views.inicio,name=('inicio')),
    #path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),
    path('quienes_somos/', TemplateView.as_view(template_name='quienes_somos.html'), name='quienes_somos'),
    path('preguntas_frecuentes/', TemplateView.as_view(template_name='preguntas_frecuentes.html'), name='preguntas_frecuentes'),
    path('contacto/', TemplateView.as_view(template_name='contacto.html'), name='contacto'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('animales/', include('animales.urls', namespace = 'animales')),
    path('refugios/', include('refugios.urls', namespace='refugios')),
    path('adoptantes/', include('adoptantes.urls', namespace='adoptantes')),
    path('adopciones/', include('adopciones.urls', namespace='adopciones')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

