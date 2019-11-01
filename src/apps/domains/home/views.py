from django.shortcuts import render
from django.views import View
from drf_yasg.utils import swagger_auto_schema

from apps.domains.home.schemas import HomeSchema
from apps.domains.home.serializers import HomeResponseSerializer
from libs.django.views.api.views import BaseApiView


class HomeView(View):
    @staticmethod
    def get(request):
        return render(request, 'home/index.html', {})


class HomeApiView(BaseApiView):
    @swagger_auto_schema(**HomeSchema.to_swagger_schema())
    def get(self, request):
        return self.success_response(data=HomeResponseSerializer({'text': 'Hello world!'}).data)
