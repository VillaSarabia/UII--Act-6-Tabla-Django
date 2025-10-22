# Expansiones/admin.py

from django.contrib import admin
from .models import Expansion # ¡IMPORTANTE! Importa tu modelo

# Registra tu modelo
admin.site.register(Expansion)