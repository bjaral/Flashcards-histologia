@echo off
REM Activar entorno virtual (ajusta la ruta si es necesario)
call .venv\Scripts\activate.bat

REM Recolectar archivos estáticos
python manage.py collectstatic --noinput

REM Aplicar migraciones
python manage.py migrate

REM Detectar sistema operativo y ejecutar el servidor apropiado
IF "%OS%"=="Windows_NT" (
    echo Ejecutando en Windows, usando servidor de desarrollo de Django...
    python manage.py runserver 0.0.0.0:8000
) ELSE (
    echo Ejecutando en sistema Unix-like, usando Gunicorn...
    gunicorn histo_udec.wsgi:application -c gunicorn_config.py
)