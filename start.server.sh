#!/bin/bash

# Recolectar archivos estáticos
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Aplicar migraciones
echo "🛠Aplicando migraciones..."
python manage.py migrate

# Iniciar el servidor con Gunicorn
echo "Iniciando servidor con Gunicorn..."
gunicorn histo_udec.wsgi:application -c gunicorn_config.py
