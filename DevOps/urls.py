"""DevOps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from all_app.user.urls import user_api_route

# root路由集合
root_router = routers.DefaultRouter()
root_router.APIRootView.__doc__ = 'DevOps接口文档'
root_router.APIRootView.__name__ = 'DevOps'
api_urls = [

]
# 用户路由
api_urls += user_api_route


# swagger 标题设置
schema_view = get_swagger_view(title='DevOps API 文档')
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^docs/', schema_view, name='docs'),
    # api接口
    url(r'^api/', include(api_urls), name='api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 媒体文件映射地址设置
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='媒体文件'),
    # 静态文件映射地址设置
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS}, name='静态文件'),
]
