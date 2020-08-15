web: gunicorn urlshortener.wsgi
release: python manage.py migrate