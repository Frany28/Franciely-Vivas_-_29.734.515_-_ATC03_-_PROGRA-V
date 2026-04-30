from django.db import models


class CityTemperature(models.Model):
    """Temperatura actual registrada para una ciudad."""

    city = models.CharField(max_length=100, unique=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city}: {self.temperature} C'
