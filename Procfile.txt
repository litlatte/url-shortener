release: python manage.py migrate
web: gunicorn urlshortener.wsgi