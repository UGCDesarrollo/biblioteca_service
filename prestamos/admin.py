from django.contrib import admin
from .models import Prestamo, UserAPIKey
from rest_framework_api_key.admin import APIKeyModelAdmin

# Registro del modelo Prestamo
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('nro_documento', 'titulo', 'autor','biblioteca_material','fecha_prestamo', 'fecha_devolucion')
    search_fields = ('nro_documento', 'titulo','autor')
    list_filter = ('titulo', 'fecha_prestamo', 'fecha_devolucion')

# Registro del modelo UserAPIKey
@admin.register(UserAPIKey)
class UserAPIKeyAdmin(APIKeyModelAdmin):
    list_display = ('name', 'user', 'created', 'revoked')
    search_fields = ('name', 'user__username')
    list_filter = ('revoked', 'created')

    # Mostrar campos adicionales en el formulario de creación
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form