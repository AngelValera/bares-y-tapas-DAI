#!/bin/bash

#Despliegue en Azure usando vagrant
sudo vagrant up --provider=azure
sudo fab -p 'Clave#Angel#1' -H vagrant@maquinaavm-service-xuybo.cloudapp.net ejecutar_app
