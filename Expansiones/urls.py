# Expansiones/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # La ruta principal (root) de la app llama a la función 'index'
]