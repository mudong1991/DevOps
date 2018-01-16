# -*- coding: utf-8 -*-
__author__ = 'Mundy'
"""
@action: 时间工具
@time: 2017/12/25 17:31
"""
import time
import datetime
from django.conf import settings


def time_calculator(atime, btime):
    """
    :param atime: 第一个时间
    :param btime: 第二个时间
    :return: 相差的秒数(a-b)
    """
    time_a = time.mktime(time.strptime(atime, settings.TIME_FORMAT))
    time_b = time.mktime(time.strptime(btime, settings.TIME_FORMAT))
    seconds = time_a - time_b
    return seconds


def time_calculator_seconds(atime, seconds):
    """
    :param atime: 第一个时间
    :param seconds: 小于这个时间的秒数
    :return: 相减格式化后的时间
    """
    time_a = time.mktime(time.strptime(atime, settings.TIME_FORMAT))
    time_b = time_a - seconds
    btime = time.strftime(settings.TIME_FORMAT, time.localtime(time_b))
    return btime


def get_current_time():
    """
    :return: 当前的时间字符串
    """
    time_string = time.strftime(settings.TIME_FORMAT, time.localtime(time.time()))
    return time_string
