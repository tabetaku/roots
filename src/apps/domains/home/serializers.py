from rest_framework import serializers

from libs.django.serializers import BaseSerializer


class HomeResponseSerializer(BaseSerializer):
    text = serializers.CharField(required=True, label='text')
