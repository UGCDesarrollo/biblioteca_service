from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrestamoViewSet

# Crear un router
router = DefaultRouter()

# Registrar el ViewSet de préstamos en el router
router.register(r'prestamos', PrestamoViewSet, basename='prestamo')

# Incluir las rutas generadas por el router
urlpatterns = [
    path('', include(router.urls)),
]