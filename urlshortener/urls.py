"""urlshortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from redurl.views import slug_view, home_view, slug_click_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls, name='home'),
    path('api/', include('redurl.urls')),
    path('account/', include('users.urls') ),
    path('<slug:slug>/', slug_view),
    path('<slug:slug>/clicks/', slug_click_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
