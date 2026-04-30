from rest_framework import serializers

from .models import CityTemperature


class CityTemperatureSerializer(serializers.ModelSerializer):
    """Serializa la temperatura registrada para una ciudad."""

    class Meta:
        model = CityTemperature
        fields = ['id', 'city', 'temperature', 'last_updated']
        read_only_fields = ['id', 'last_updated']
