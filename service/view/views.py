from django.db import models
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from service.service_filter import ServiceFilter
from service.models import Service
from service.serializers.service_serializer import ServiceSerializer
from .tracking_mixin import TrackingMixinView


# class ServiceViewSet(TrackingMixinView, viewsets.ModelViewSet):
class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    search_fields = ('name',)
    ordering_fields = ['name', 'category', 'price', 'os_platform']
    filterset_class = ServiceFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_fields = ('name', 'category')
