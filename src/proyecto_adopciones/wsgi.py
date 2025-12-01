"""
WSGI config for adopciones project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_adopciones.settings')

from .initial_data import load_initial_data_if_needed
load_initial_data_if_needed()

application = get_wsgi_application()
