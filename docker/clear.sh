#!/bin/bash
echo "stop django-operations ---------------------"
docker stop taileizi
sudo docker ps -a | awk '{ print $1,$2 }' | grep mudong/taileizi| awk '{print $1 }' | xargs -I {} sudo docker rm {}
docker rm -f taileizi
docker rmi -f mudong/taileizi
