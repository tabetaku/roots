from drf_yasg import openapi

from apps.domains.home.serializers import HomeResponseSerializer
from libs.django.swagger.schemas import BaseSchema


class HomeSchema(BaseSchema):
    operation_id = 'home'
    operation_description = 'Home'
    responses = {
        '200': openapi.Response('success', schema=HomeResponseSerializer(), ),
        '401': openapi.Response(description='Not Authorized')
    }
