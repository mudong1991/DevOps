from datetime import datetime

from django.db import models
from core.models import CoreModel
from utils.permission_classes import custom_model_permission


def upload_path(instance, filename):
    return 'upload/{}/{}/{}/{}'.format(instance.category, datetime.now().year, datetime.now().month, filename)


class File(CoreModel):
    file = models.FileField(upload_to=upload_path, verbose_name='文件')
    category = models.CharField(max_length=100, verbose_name='文件类别')

    class Meta:
        verbose_name = verbose_name_plural = '文件'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])


class Province(CoreModel):
    """省"""
    name = models.CharField(max_length=255, verbose_name='名称')
    short_name = models.CharField(max_length=255, blank=True, verbose_name='简称')
    lng = models.CharField(max_length=255, blank=True, verbose_name='经度')
    lat = models.CharField(max_length=255, blank=True, verbose_name='纬度')
    pinyin = models.CharField(max_length=255, blank=True, verbose_name='拼音')
    zip_code = models.CharField(max_length=255, blank=True, verbose_name='邮编')
    area_code = models.CharField(max_length=255, blank=True, verbose_name='区域编码')
    merger_name = models.CharField(max_length=255, blank=True, verbose_name='合并名称')
    city_code = models.CharField(max_length=255, blank=True, verbose_name='城市编码')

    class Meta:
        verbose_name = verbose_name_plural = '省'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])

    def __str__(self):
        return self.name


class City(CoreModel):
    """市"""
    province = models.ForeignKey(Province, related_name='cities', verbose_name='省')
    name = models.CharField(max_length=255, verbose_name='名称')
    short_name = models.CharField(max_length=255, blank=True, verbose_name='简称')
    lng = models.CharField(max_length=255, blank=True, verbose_name='经度')
    lat = models.CharField(max_length=255, blank=True, verbose_name='纬度')
    pinyin = models.CharField(max_length=255, blank=True, verbose_name='拼音')
    zip_code = models.CharField(max_length=255, blank=True, verbose_name='邮编')
    area_code = models.CharField(max_length=255, blank=True, verbose_name='区域编码')
    merger_name = models.CharField(max_length=255, blank=True, verbose_name='合并名称')
    city_code = models.CharField(max_length=255, blank=True, verbose_name='城市编码')

    class Meta:
        verbose_name = verbose_name_plural = '市'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])

    def __str__(self):
        return self.name


class County(CoreModel):
    """县"""
    city = models.ForeignKey(City, related_name='counties', null=True, verbose_name='市')
    name = models.CharField(max_length=255, blank=True, verbose_name='名称')
    short_name = models.CharField(max_length=255, blank=True, verbose_name='简称')
    lng = models.CharField(max_length=255, blank=True, verbose_name='经度')
    lat = models.CharField(max_length=255, blank=True, verbose_name='纬度')
    pinyin = models.CharField(max_length=255, blank=True, verbose_name='拼音')
    zip_code = models.CharField(max_length=255, blank=True, verbose_name='邮编')
    area_code = models.CharField(max_length=255, blank=True, verbose_name='区域编码')
    merger_name = models.CharField(max_length=255, blank=True, verbose_name='合并名称')
    city_code = models.CharField(max_length=255, blank=True, verbose_name='城市编码')

    class Meta:
        verbose_name = verbose_name_plural = '区县'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])

    def __str__(self):
        return self.name

