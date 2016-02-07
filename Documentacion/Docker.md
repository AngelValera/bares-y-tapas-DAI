##**Entorno de pruebas**##

Lo primero que debemos hacer es crear en el directorio raíz del proyecto un fichero llamado **[Dockerfile](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Dockerfile)**, en el que incluimos todo lo necesario para preparar la imagen, tenemos que indicar el sistema operativo que en mi caso, es una imagen Ubuntu oficial, además le indico que actualice los repositorios, que instale los paquetes necesarios de Python, se descargue el repositorio de la aplicación, instale las dependencias y realice las migraciones de bases de datos necesarias.

Hecho esto debemos registrarnos en dockerHub y unir la cuenta de github.

![](http://i666.photobucket.com/albums/vv21/angelvalera/hito4/Seleccioacuten_001_zpseqsayqpm.png)

Ahora le damos a **Create** y a **Automated Build** y seleccionamos el repositorio de nuestro proyecto, escribimos una descripción y pulsamos en create.

![](http://i666.photobucket.com/albums/vv21/angelvalera/hito4/Seleccioacuten_002_zpszd1a3clk.png)

Hecho esto le indicamos que se automatizará con cada push sobre la rama, para ello pulsamos el botón Trigger en el menú Building Settings.

![](http://i666.photobucket.com/albums/vv21/angelvalera/hito4/Seleccioacuten_003_zpspbqpn3ox.png)

Podemos ver que se crea la imagen correctamente:

![](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/Seleccioacuten_010_zpsmks0nng6.png)

[Imagen en DockerHub](https://hub.docker.com/r/angelvalera/bares-y-tapas-dai/)

Ahora podemos descargarla y ejecutarla:

* Para descargar la imagen:

**```docker pull angelvalera/bares-y-tapas-dai```**

* Para iniciar la imagen y ejecutar la aplicación:

**```sudo docker run -i -t angelvalera/bares-y-tapas-dai /bin/bash```**

**```cd /bares-y-tapas-DAI/```**

**```ifconfig```**

**```python manage.py runserver 0.0.0.0:2222 &```**

Una vez que sabemos la ip y el puerto desde el navegador podemos acceder a ella.

Para automatizar todo este proceso, he creado un script **[docker.sh](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Scripts/docker.sh)**, cuyo contenido es:

```
#!/bin/bash
#Descarga docker
sudo apt-get update
sudo apt-get install -y docker.io
# Inicia el servicio docker
sudo service docker start
sudo docker -d &
# Descarga la imagen
docker pull angelvalera/bares-y-tapas-dai
# Ejecuta la imagen
sudo docker run -i -t angelvalera/bares-y-tapas-dai /bin/bash
```

Si ejecutamos este script,(habiéndole dado permiso de ejecución) nos ejecuta la imagen, con lo que tenemos que acceder al directorio del proyecto y lanzarla:

```
cd ..
sudo python manage.py runserver 0.0.0.0:2222 &
```

He creado otro script llamado **[ejecutar_App.sh](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Scripts/ejecutar_App.sh)**, que ejecuta la aplicación una vez que estamos dentro del direcctorio de la aplicación, por ejemplo:

```
./docker.sh
cd /proyectoiv-modulo-1/
cd /Scripts/
./ejecutar_App.sh
```
Podemos comprobar que realmente todo funciona:
![](http://i666.photobucket.com/albums/vv21/angelvalera/hito4/Seleccioacuten_005_zps6csk7sy7.png)