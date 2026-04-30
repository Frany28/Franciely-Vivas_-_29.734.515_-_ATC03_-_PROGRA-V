from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets

from .models import CityTemperature
from .serializers import CityTemperatureSerializer


temperature_response = openapi.Response(
    description='Registro de temperatura de una ciudad.',
    schema=CityTemperatureSerializer,
    examples={
        'application/json': {
            'id': 1,
            'city': 'Caracas',
            'temperature': '28.50',
            'last_updated': '2026-04-30T18:00:00Z',
        }
    },
)

temperature_list_response = openapi.Response(
    description='Listado de temperaturas registradas.',
    schema=CityTemperatureSerializer(many=True),
    examples={
        'application/json': [
            {
                'id': 1,
                'city': 'Caracas',
                'temperature': '28.50',
                'last_updated': '2026-04-30T18:00:00Z',
            },
            {
                'id': 2,
                'city': 'Valencia',
                'temperature': '30.20',
                'last_updated': '2026-04-30T18:05:00Z',
            },
        ]
    },
)

not_found_response = openapi.Response(
    description='No existe un registro de temperatura con el ID indicado.',
    examples={
        'application/json': {
            'detail': 'No encontrado.',
        }
    },
)

created_response = openapi.Response(
    description='Registro de temperatura creado correctamente.',
    schema=CityTemperatureSerializer,
    examples={
        'application/json': {
            'id': 3,
            'city': 'Maracay',
            'temperature': '29.75',
            'last_updated': '2026-04-30T18:10:00Z',
        }
    },
)

validation_error_response = openapi.Response(
    description='Datos invalidos o ciudad duplicada.',
    examples={
        'application/json': {
            'city': ['city temperature with this city already exists.'],
        }
    },
)


class CityTemperatureViewSet(viewsets.ModelViewSet):
    """
    Endpoints CRUD para administrar temperaturas por ciudad.

    Permite listar, consultar, crear, actualizar y eliminar registros de
    temperatura. Las consultas son publicas y las escrituras requieren
    autenticacion por token.
    """

    queryset = CityTemperature.objects.all()
    serializer_class = CityTemperatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary='Listar temperaturas',
        operation_description=(
            'Devuelve todos los registros de temperatura guardados en la API.'
        ),
        responses={200: temperature_list_response},
        tags=['Temperaturas'],
    )
    def list(self, request, *args, **kwargs):
        """Lista todas las temperaturas registradas."""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Consultar una temperatura',
        operation_description=(
            'Obtiene el registro de temperatura asociado al ID enviado en la URL.'
        ),
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description='ID numerico del registro de temperatura.',
                type=openapi.TYPE_INTEGER,
                example=1,
            )
        ],
        responses={200: temperature_response, 404: not_found_response},
        tags=['Temperaturas'],
    )
    def retrieve(self, request, *args, **kwargs):
        """Consulta una temperatura por ID."""
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Crear temperatura',
        operation_description=(
            'Crea un nuevo registro indicando ciudad y temperatura actual.'
        ),
        request_body=CityTemperatureSerializer,
        responses={201: created_response, 400: validation_error_response},
        tags=['Temperaturas'],
    )
    def create(self, request, *args, **kwargs):
        """Crea un registro de temperatura."""
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Actualizar temperatura',
        operation_description=(
            'Reemplaza completamente los datos de un registro existente.'
        ),
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description='ID numerico del registro a actualizar.',
                type=openapi.TYPE_INTEGER,
                example=1,
            )
        ],
        request_body=CityTemperatureSerializer,
        responses={
            200: temperature_response,
            400: validation_error_response,
            404: not_found_response,
        },
        tags=['Temperaturas'],
    )
    def update(self, request, *args, **kwargs):
        """Actualiza todos los campos editables de una temperatura."""
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Actualizar parcialmente temperatura',
        operation_description=(
            'Actualiza uno o varios campos editables de un registro existente.'
        ),
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description='ID numerico del registro a modificar.',
                type=openapi.TYPE_INTEGER,
                example=1,
            )
        ],
        request_body=CityTemperatureSerializer,
        responses={
            200: temperature_response,
            400: validation_error_response,
            404: not_found_response,
        },
        tags=['Temperaturas'],
    )
    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente una temperatura."""
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Eliminar temperatura',
        operation_description='Elimina un registro de temperatura por ID.',
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description='ID numerico del registro a eliminar.',
                type=openapi.TYPE_INTEGER,
                example=1,
            )
        ],
        responses={204: 'Registro eliminado correctamente.', 404: not_found_response},
        tags=['Temperaturas'],
    )
    def destroy(self, request, *args, **kwargs):
        """Elimina una temperatura por ID."""
        return super().destroy(request, *args, **kwargs)
