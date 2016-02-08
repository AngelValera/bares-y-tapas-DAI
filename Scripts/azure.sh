#Despliegue en Azure usando vagrant
cd ../despliegueAzure/
vagrant up --provider=azure
fab -p 'Clave#Angel#1' -H vagrant@maquinaavm-service-xuybo.cloudapp.net ejecutar_app
