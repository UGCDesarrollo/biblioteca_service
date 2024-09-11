from django.db import models
from django.contrib.auth.models import User
from rest_framework_api_key.models import APIKey

class UserAPIKey(APIKey):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Prestamo(models.Model):
    Nro_Documento = models.CharField(max_length=40)  # Identificación de la persona
    Titulo = models.TextField()    # Identificador del libro
    Autor = models.TextField()    # Identificador del libro
    Biblioteca_material = models.CharField(max_length=40)
    Fecha_prestamo = models.DateTimeField(null=True, blank=True)  # Fecha del préstamo
    Fecha_devolucion = models.DateTimeField(null=True, blank=True)  # Fecha de devolución
    
    class Meta:
        db_table = 'temporal_etl'
    def __str__(self):

        return f"Préstamo {self.Nro_Documento} - Libro {self.Titulo}"

