from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import RedUrlSerializer
from django.utils import timezone
from .models import RedUrl, Click
from django.contrib.auth.models import User
import string
import random




# Create your views here.
@api_view(['CREATE', 'POST'])
@permission_classes((permissions.AllowAny, ))
def create_slug(request, *args, **kwargs):
    serializer = RedUrlSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        obj = serializer.validated_data
    
        if not request.user.is_authenticated:
            if obj['slug'] != '':
                return Response({"message": "Login to use a custom slug, or use a random generated one"}, 403)
        if obj['slug'] == '':
            obj['slug'] = ''.join(random.choices(string.ascii_letters+string.digits, k=7))    
        obj['created']  = timezone.now()
        obj['ip_creator']  = request.META['REMOTE_ADDR']
        if request.user.is_authenticated:
            obj['user_creator'] = request.user
            request.user.slugs.add(serializer.save())
        else:
            serializer.save()
        return Response({"url": serializer.validated_data["url"], "slug": serializer.validated_data["slug"]}, 201)
    return Response({}, 400)




def slug_click_view(request, slug, *args, **kwargs):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    else:
        obj = get_object_or_404(RedUrl, slug=slug)
        obj = request.user.slugs.filter(slug=slug)
        
        if not obj:
            return HttpResponseForbidden()
        obj = obj.first()
        ctx = {
            'slug': slug,
            'clicks': obj.clicks.all()
        }
        
        return render(request, 'registration/click.html', context=ctx)
def slug_view(request, slug, *args, **kwargs):
    obj = get_object_or_404(RedUrl, slug=slug)
    if request.user.is_authenticated:
        obj.clicks.add(Click.objects.create(slug=obj, user_click=request.user, ip=request.META['REMOTE_ADDR'], timestamp=timezone.now()))
    obj.clicks.add(Click.objects.create(slug=obj, ip=request.META['REMOTE_ADDR'], timestamp=timezone.now()))
    return redirect(obj.url)

def home_view(request, *args, **kwargs):
    return render(request, 'home.html')
