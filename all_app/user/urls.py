# -*- coding: utf-8 -*-
__author__ = 'Mundy'
"""
@action: 用户相关路由
@time: 2017/12/19 16:29
"""
from django.conf.urls import url
from utils.custom_router import CustomRouter
from user.views import *


# ----------------独立路由------------------
urlpatterns = [

]

# ------------------路由集合----------------
router = CustomRouter()
"""用户管理"""
router.register(r'user', UserViewSet, base_name='user')

# ------------------路由接口----------------
user_api_route = router.urls + urlpatterns

