from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

from api import serializers
from map.models import HuntingSpot


# Create your views here.
class HuntingViewSet(viewsets.ModelViewSet):
    queryset = HuntingSpot.objects.all()
    serializer_class = serializers.HuntingSerializer
