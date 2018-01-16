# -*- coding: utf-8 -*-
__author__ = 'Mundy'
"""
@action: 通用工具
@time: 2017/12/25 17:31
"""
import os
import tarfile


def make_tar(file_name, source_dir):
    """
    将目录打包成tar
    :param file_name: 文件名字，可以是路径，文件名必须是tar后缀
    :param source_dir: 打包的目录路径
    :return:
    """
    with tarfile.open(file_name, "w") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def make_tar_gz(file_name, source_dir):
    """
    将目录打包压缩成tar.gz
    :param file_name: 文件名字，可以是路径，文件名必须是tar.gz后缀
    :param source_dir: 打包的目录路径
    :return:
    """
    with tarfile.open(file_name, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))