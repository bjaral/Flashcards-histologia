# gunicorn_config.py

bind = "0.0.0.0:8000"
workers = 3
timeout = 120

# Mostrar logs en consola (lo que Render captura)
accesslog = "-"
errorlog = "-"
