# -*- coding: utf-8 -*-
__author__ = 'Mundy'
"""
@action: 
@time: 2017/12/25 12:02
"""
from rest_framework import routers
from collections import OrderedDict


class CustomRouter(routers.DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name

        for prefix, viewset, basename in self.registry:
            if viewset.__doc__ is None:
                api_root_dict[prefix] = list_name.format(basename=basename)
            else:
                api_root_dict[viewset.__doc__] = list_name.format(basename=basename)

        return self.APIRootView.as_view(api_root_dict=api_root_dict)