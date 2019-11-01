from rest_framework.views import APIView

from libs.django.views.api.mixins import ResponseMixin


class BaseApiView(ResponseMixin, APIView):
    pass
