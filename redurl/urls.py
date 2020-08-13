from django.urls import path
from .views import create_slug

urlpatterns = [
    path('create/', create_slug, name='api_create'),
]