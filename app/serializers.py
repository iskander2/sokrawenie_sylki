from rest_framework import serializers
from .models import Url
    


class UrlSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Url
        fields = '__all__'


class UrlCreatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Url
        fields = ['origin_url',]

