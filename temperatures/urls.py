from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CityTemperatureViewSet

router = DefaultRouter()
router.register(r'temperatures', CityTemperatureViewSet, basename='temperature')

urlpatterns = [
    path('', include(router.urls)),
]
