from django.shortcuts import render
from .models import Expansion # Importa el modelo

def index(request):
    # Obtiene todos los registros de la tabla Expansion
    expansiones = Expansion.objects.all() 
    
    # Prepara el contexto para enviarlo a la plantilla
    context = {
        'lista_expansiones': expansiones
    }
    
    return render(request, 'index.html', context)