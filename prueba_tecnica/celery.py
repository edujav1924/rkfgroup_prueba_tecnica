# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define el nombre de tu aplicación Django y establece la configuración de Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba_tecnica.settings')
app = Celery('prueba_tecnica')

# Lee la configuración de Django para Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre automáticamente tareas en la aplicación Django
app.autodiscover_tasks()
