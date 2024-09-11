from rest_framework import viewsets
from .models import Prestamo
from rest_framework_api_key.permissions import HasAPIKey
from .serializers import PrestamoSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# from django_ratelimit.decorators import ratelimit


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['Nro_Documento']
    search_fields = ['Titulo','Autor','Biblioteca_material']  # Permitir búsquedas por identificación de la persona
    # http_method_names = ['get']  # Solo permitir GET (listar y ver)
    
    # @ratelimit(key='ip', rate='5/m')  # Limitar a 5 solicitudes por minuto
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)