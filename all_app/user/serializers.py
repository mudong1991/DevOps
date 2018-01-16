# -*- coding: utf-8 -*-
__author__ = 'Mundy'
"""
@action: 用户序列化
@time: 2017/12/25 11:08
"""
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """用户序列化"""
    class Meta:
        model = User
        fields = '__all__'
