from rest_framework import serializers
from .models import CityTemperature

class CityTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityTemperature
        fields = '__all__'