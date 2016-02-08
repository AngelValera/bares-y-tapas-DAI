#!/bin/bash

#Despliegue en Azure usando vagrant
cd ../despliegueAzure
sudo vagrant up --provider=azure
cd ..
sudo fab -p 'Clave#Angel#1' -H vagrant@maquinaavm-service-xuybo.cloudapp.net ejecutar_app
