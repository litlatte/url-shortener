from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    slugs = models.ManyToManyField('redurl.RedUrl', related_name='slugs',blank=True )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username