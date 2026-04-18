from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

# Create your views here.

class CityTemperatureViewSet(viewsets.ModelViewSet):
    queryset = CityTemperature.objects.all()
    serializer_class = CityTemperatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
