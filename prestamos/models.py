from django.db import models
from django.contrib.auth.models import User
from rest_framework_api_key.models import APIKey

class UserAPIKey(APIKey):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Prestamo(models.Model):
    nro_documento = models.CharField(max_length=40,verbose_name="nro_documento",null=True, blank=True,)  # Identificación de la persona
    titulo = models.TextField(verbose_name="titulo",null=True, blank=True,)    # Identificador del libro
    autor = models.TextField(verbose_name="autor",null=True, blank=True,)    # Identificador del libro
    biblioteca_material = models.CharField(max_length=40,verbose_name="biblioteca_material",null=True, blank=True,)
    fecha_prestamo = models.DateTimeField(null=True, blank=True,verbose_name="fecha_prestamo")  # Fecha del préstamo
    fecha_devolucion = models.DateTimeField(null=True, blank=True,verbose_name="fecha_devolucion")  # Fecha de devolución
    
    class Meta:
        db_table = 'temporal_etl'
    def __str__(self):

        return f"Préstamo {self.nro_documento} - Libro {self.titulo}"

