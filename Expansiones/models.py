from django.db import models

class Expansion(models.Model):
    # ID_Expansion es automático por defecto (id), pero si lo requieres explícito:
    # ID_Expansion = models.AutoField(primary_key=True) 
    Nombre_expansion = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    total_cartas = models.IntegerField()
    idioma = models.CharField(max_length=50)
    activa = models.BooleanField(default=True) # Indica si la expansión está activa/vigente

    def __str__(self):
        return self.Nombre_expansion