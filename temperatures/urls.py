from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityTemperatureViewSet

router = DefaultRouter()
router.register(r'temperatures', CityTemperatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]