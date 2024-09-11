#!/bin/sh

# Ejecutar migraciones
echo "Ejecutando makemigrations para todas las apps..."
python manage.py makemigrations --noinput

echo "Ejecutando makemigrations específicamente para la app 'prestamos'..."
python manage.py makemigrations prestamos --noinput

echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Recolectar archivos estáticos
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Iniciar Gunicorn para servir la aplicación Django
echo "Iniciando Gunicorn..."
gunicorn biblioteca_service.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=info \
    --timeout 300 \
    --access-logfile - &

# Mantener el contenedor activo
echo "Manteniendo el contenedor activo..."
tail -f /dev/null
