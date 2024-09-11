from .settings import *  # Hereda todas las configuraciones de settings.py
from decouple import config

import os
# Desactivar el modo DEBUG en producción
DEBUG = config('DEBUG', default=False, cast=bool)

# Hosts permitidos (añade los dominios de producción)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='.localhost,.tudominio.com').split(',')

# Seguridad para la clave secreta (siempre usando variables de entorno)
SECRET_KEY = config('SECRET_KEY')

# Configura los orígenes permitidos (CORS) en producción
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='', cast=lambda v: [s.strip() for s in v.split(',')])

# Configuración de la base de datos para producción (PostgreSQL en este caso)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Configuración de archivos estáticos en Django
STATIC_URL = '/servicio/biblioteca/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de archivos de media (si también es necesario)
MEDIA_URL = '/servicio/biblioteca/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Configuración de seguridad específica de Django

# Redirección a HTTPS si está detrás de un proxy inverso como Nginx
SECURE_SSL_REDIRECT = True

# Confiar en el encabezado "X-Forwarded-Proto" del proxy para determinar si la conexión es segura
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Seguridad de las cookies: solo enviarlas a través de HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Protección contra ataques XSS y clickjacking
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Configuración de HSTS (puedes dejar que Nginx lo maneje, o mantenerlo en Django)
SECURE_HSTS_SECONDS = 31536000  # 1 año
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Configuración para servir archivos estáticos con WhiteNoise (opcional si Nginx maneja estáticos)
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise para servir archivos estáticos
    *MIDDLEWARE,  # Incluye el middleware original de settings.py
]

# WhiteNoise para la compresión de archivos estáticos (opcional si Nginx maneja estáticos)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración de DRF
if DEBUG:
    # Si estás en desarrollo, permites la API navegable de DRF
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',  # Permitir navegación solo en desarrollo
        )
    }
else:
    # En producción, solo devuelve respuestas JSON
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        )
    }