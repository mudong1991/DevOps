FROM daocloud.io/python:2.7
MAINTAINER mudong  <blog.scmud.com>
ENV PYPYTHONUNBUFFERED 1
ADD TaiWeb.tar /var/www/TaiWeb
WORKDIR /var/www/TaiWeb
RUN pip install  -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
