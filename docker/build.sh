#!/bin/bash
echo "Packaging taileizi project ......"
rm ./TaiWeb.tar -rf
tar -cf TaiWeb.tar -C ../ ./
echo "Build mudong/taileizi docker image start ......"
docker build -t mudong/taileizi ./
echo "Start container taileizi ......"
docker run --name taileizi -v /var/www/TaiWeb:/var/www/TaiWeb --net=host -d mudong/taileizi /usr/local/bin/uwsgi --ini uwsgi-taileizi.ini
