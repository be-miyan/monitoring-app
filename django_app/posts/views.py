from rest_framework import generics

from rpzsensor.models import Environment, Photo
from .serializers import EnvironmentSerializer, PhotoSerializer

class RecordPost(generics.ListCreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

class PhotoPost(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
