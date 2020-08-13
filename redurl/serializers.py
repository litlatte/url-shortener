from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import RedUrl

class RedUrlSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, default='', validators=[UniqueValidator(queryset=RedUrl.objects.all())])
    class Meta:
        model = RedUrl
        
        fields = ['url', 'slug']