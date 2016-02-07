#!/bin/bash

#Descarga docker
sudo apt-get update
sudo apt-get install -y docker.io
# Inicia el servicio docker
sudo service docker start
sudo docker -d &
#Descarga la imagen
docker pull angelvalera/bares-y-tapas-dai
#Ejecuta la imagen
sudo docker run -i -t angelvalera/bares-y-tapas-dai /bin/bash
