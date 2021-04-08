from rest_framework import serializers

from rpzsensor.models import Environment, Photo


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ('postdate', 'place', 'temperature', 'pressure', 'humidity', 'lux')
    
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo 
        fields = ('title', 'image', 'postdate', 'place')
