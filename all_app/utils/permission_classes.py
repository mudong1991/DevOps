# -*- coding: utf-8 -*-
__author__ = 'Mundy'
"""
@action: 
@time: 2018/1/15 11:06
"""
from rest_framework import permissions
from django.utils.encoding import force_text
from django.conf import settings


def custom_model_permission(model_name, verbose_name, action_list=None):
    """
    :param action_list: 权限方法列表
    :param model_name: 模型名字（cls.__name__.lower()）
    :param verbose_name: model verbose_name
    :return: 模型权限名称列表
    """
    action_dict = settings.ACTION_DICT

    if action_list is None:
        action_list = []
    return [('%s_%s' % (action, model_name.lower()), '%s %s' % (action_dict[action], force_text(verbose_name))) for action in action_list]


# 模型的权限
class ModelPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.read_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }