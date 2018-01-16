import json
import pandas
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common import serializers
from common.models import City, County, File, Province
from common.serializers import CitySerializer, CountySerializer, FileSerializer, ProvinceSerializer, SmsSerializer


class FileViewSet(viewsets.ModelViewSet):
    """文件"""
    queryset = File.objects.all()
    serializer_class = FileSerializer
    """身份认证的权限"""
    permission_classes = (IsAuthenticated,)


class ProvinceViewSet(viewsets.ModelViewSet):
    """省"""
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()
    pagination_class = None

    def perform_update(self, serializer):
        instance = serializer.save()
        cities = City.objects.filter(province=instance)
        cities.update(level=instance.level)
        County.objects.filter(city__in=cities).update(level=instance.level)


class CityViewSet(viewsets.ModelViewSet):
    """市"""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_fields = ('province',)
    pagination_class = None

    def perform_update(self, serializer):
        instance = serializer.save()
        County.objects.filter(city=instance).update(level=instance.level)


class CountyViewSet(viewsets.ModelViewSet):
    """县"""
    queryset = County.objects.all()
    serializer_class = CountySerializer
    pagination_class = None
    filter_fields = ('city',)
