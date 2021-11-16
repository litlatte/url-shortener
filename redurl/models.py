from django.db import models
from django.conf import settings

def get_deleted_user_instance():
    return settings.AUTH_USER_MODEL.objects.get(username='deleted', email='deleted@deleted.del')

# Create your models here.
class Click(models.Model):
    id = models.AutoField(primary_key=True)
    user_click = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET(get_deleted_user_instance))
    slug = models.ForeignKey("RedUrl", on_delete=models.CASCADE)
    ip = models.fields.GenericIPAddressField()
    timestamp = models.fields.DateTimeField()

class RedUrl(models.Model):
    id = models.AutoField(primary_key=True)
    user_creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET(get_deleted_user_instance))
    slug = models.SlugField(unique=True)
    url = models.URLField()
    ip_creator = models.GenericIPAddressField()
    created = models.DateTimeField()
    clicks = models.ManyToManyField(Click, related_name="clicks", blank=True)
