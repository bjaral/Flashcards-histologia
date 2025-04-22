# gunicorn_config.py

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
workers = 3
timeout = 120

# Mostrar logs en consola (lo que Render captura)
accesslog = "-"
errorlog = "-"
