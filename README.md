[![resultado del test](https://travis-ci.org/AngelValera/bares-y-tapas-DAI.svg?branch=master)](https://travis-ci.org/AngelValera/bares-y-tapas-DAI)

[![SnapCI](https://snap-ci.com/AngelValera/bares-y-tapas-DAI/branch/master/build_image)](https://snap-ci.com/AngelValera/bares-y-tapas-DAI/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://appbaresytapas.herokuapp.com/)

[![Docker](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/dockericon_zps5smgqzbv.png)](https://hub.docker.com/r/angelvalera/bares-y-tapas-dai/)

[![Azure](http://azuredeploy.net/deploybutton.png)](http://maquinaavm-service-xuybo.cloudapp.net
)

#**BARES Y TAPAS**#
## **Proyecto de Infraestructura Virtual junto con Desarrollo de Aplicaciones para Internet** ##

**Descripción:**

Aplicación desarrollada para las asignaturas de infraestructura virtual y desarrollo de aplicaciones para internet, se trata de una webb donde podemos registrar varios bares y tapas de dichos bares. Los usuarios registrados pueden añadir y visitar los bares que quieran y así como las tapas que quieran incluir a un bar, además de poder darles un voto, en la página principal se mostrará los 5 bares con más visitas así como las tapas más puntuadas.

He elegido llevar a cabo este proyecto, porque se centra en la virtualización de recursos como puede ser el uso de máquinas virtuales para el despliegue de una aplicación para Internet, usando también para ello un framework de alto nivel.

**Estoy inscrito en el certamen de proyectos de la UGR organizado por la OSL.**

##**Estructura del proyecto**##
Al tratarse de un proyecto python, desarrollado en django, tenemos tres directorios principales:

* **Proyecto_DAI:** que contiene los ficheros referentes al proyecto python .

* **app:** que contiene los ficheros referentes a nuestra aplicación y que usa a su vez los del fichero "Proyecto_DAI"

* **templates/app:** Contiene los templates que usa la aplicación de bares y tapas.

* **media/bar:** Contiene las imágenes de la tapa de cada bar que el usuario sube. 

##**Instalación local de la aplicación**##

Tenemos que ejecutar lo siguiente:

```
git clone https://github.com/AngelValera/bares-y-tapas-DAI
cd bares-y-tapas-DAI
python manage.py migrate
python manage.py runserver
```
##**1-Integración continua**##

Para la integración continua he utilizado travis, ya que es el que me ha resultado más sencillo de utilizar junto con github.

Para las pruebas, usamos el fichero **[test.py](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/app/tests.py)** y para su ejecución usamos la herramienta manage.py :

```
python manage.py test ó python manage.py test nombreaplicacion
```

Estos test se usarán tanto en el despliegue en un Paas como en la integración continua.


[Más Información](https://github.com/AngelValera/proyectoIV-Modulo-1/blob/master/Documentacion/IntCont.mds)


##**2-Despliegue en un PaaS Heroku**##

El siguiente paso es desplegar nuestra aplicación en un Paas, he utilizado heroku, lo he escogido porque aprendí a utilizarlo con los ejercicios del tema 3 y me resultó sencillo de usar, además de porque necesita un fichero de configuración que describe la infraestructura virtual. Se añade además un script de automatización **[heroku.sh](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Scripts/heroku.sh)**.

La aplicación podemos verla funcionando [aquí](http://appbaresytapas.herokuapp.com/).

[Más Información](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Documentacion/PAAS.md)


##**3-Entorno de pruebas**##

Para el entorno de pruebas se ha utilizado Docker el cual está basado en un sistema de contenedores. Para su uso, he creado una imagen basada en Ubuntu la cual tiene la aplicación de bares y tapas descargada y preparada para su ejecución y la cual puede ser obtenida con una sola orden desde [DockerHub](https://hub.docker.com/r/angelvalera/bares-y-tapas-dai/). Se añade además un script de automatización **[docker.sh](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Scripts/docker.sh)**.

[Más Información](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Documentacion/Docker.md)


##**4-Despliegue en un IaaS AZURE**##


Para el despliegue de la aplicación en un IaaS, he decidido usar Vagrant para la creación de máquinas virtuales, y Ansible para el provisionamiento de dichas máquinas virtuales, los elijo porque me han resultado más fáciles de usar que por ejemplo chef y su árbol específico de directorios. Las máquinas virtuales se crearán en una cuenta de Azure, configurada correctamente.

Para instalar tanto vagrant como ansible se proporiona un script llamado **[install_Azure_Vagrant.sh](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Scripts/install_Azure_Vagrant.sh)** y para desplegar la aplicación completa en una máquina de azure se proporciona otro script llamado **[azure.sh](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Scripts/azure.sh)**


La aplicación podemos verla funcionando [aquí](http://maquinaavm-service-xuybo.cloudapp.net/).


[Más Información](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Documentacion/IAAS.md)













