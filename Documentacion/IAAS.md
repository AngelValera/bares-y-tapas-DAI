##**4-Despliegue en un IaaS AZURE**##


Para el despliegue de la aplicación en un IaaS, he decidido usar Vagrant para la creación de máquinas virtuales, y Ansible para el provisionamiento de dichas máquinas virtuales, los elijo porque me han resultado más fáciles de usar que por ejemplo chef y su árbol específico de directorios. Las máquinas virtuales se crearán en una cuenta de Azure, configurada correctamente.

* Para configurar nuestra cuenta de azure correctamente lo primero que tenemos que hacer es instalar es el provisionador azure para vagrant

```vagrant plugin install vagrant-azure```

![](http://i666.photobucket.com/albums/vv21/angelvalera/Ejercicios%20tema%206/Seleccioacuten_023_zpsrddsrwg7.png)


* El siguiente paso es loguearse y conseguir información de las credenciales de Azure:

```
azure login
azure account download
```

![](http://i666.photobucket.com/albums/vv21/angelvalera/Ejercicios%20tema%206/Seleccioacuten_024_zpsdfxi5axe.png)

```azure account import Evaluación\ gratuita-2-5-2016-credentials.publishsettings```

![](http://i666.photobucket.com/albums/vv21/angelvalera/Ejercicios%20tema%206/Seleccioacuten_025_zpsqvr4qpfj.png)


* Lo siguiente que debemos hacer es generar los certificados que se van a subir a Azure:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azurevagrant.key -out azurevagrant.key
chmod 600 azurevagrant.key
openssl x509 -inform pem -in azurevagrant.key -outform der -out azurevagrant.cer
```

* Lo siguiente es subir el archivo .cer a Azure:

![](http://i666.photobucket.com/albums/vv21/angelvalera/Ejercicios%20tema%206/Seleccioacuten_026_zpslehlmd7g.png)

* Para autenticar la maquina azure desde el Vagrantfile, necesitamos un archivo.pem. Para generarlo necesitamos hacer un truco, primero ejecutar:

```
openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem
```

* Para generarlo y después concatenarle el fichero.key. Esto es necesario para que el fichero.pem contenga tanto la clave publica como la privada.

```
cat azurevagrant.key > azurevagrant.pem 
```
* Ahora lo que debemos hacer es crear el [vagrantfile](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/despliegueAzure/Vagrantfile):

```
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.vm.box = "azure"
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  config.vm.network "public_network"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.define "localhost" do |l|
          l.vm.hostname = "localhost"
  end
  config.vm.provider :azure do |azure, override|
    azure.mgmt_certificate = '/home/angel/Prueba/azurevagrant.pem'
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = '8afb40f4-4482-4a5c-832a-b7aab655fed1'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
    azure.vm_name = 'maquinaavm2'
    azure.cloud_service_name = 'maquinaavm2'
    azure.vm_password = 'Clave#Angel#1'
    azure.vm_location = 'Central US'
        azure.ssh_port = '22'
        azure.tcp_endpoints = '80:80'
  end
  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "playbookIV.yml"
        ansible.verbose = "v"
  end
end
```

Podemos ver que en la primera parte del vagrantfile indicamos la box que debe usar, así com la red pública que tendrá, además de la redirección de puertos.

En la segunda parte indicamos los datos del usuario que quiere desplegar la aplicación, en este caso, los mios, debemos indicar donde está el certificado que creamos antes, así como nuestro identificador de subcripción de azure, la imagen de SO que queremos que use la máquina virtual y nuestro usuario y contraseña.

Por último indicamos que provisione la máquina usando el playbook de ansible, en este caso el siguiente:

* Ahora definimos el [playbook](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/despliegueAzure/playbookIV.yml) de ansible:

```YML
- hosts: localhost
  remote_user: vagrant
  become: yes
  become_method: sudo
  tasks:
  - name: Actualizar repositorios
    apt: update_cache=yes
  - name: Instalar dependencias
    apt: name={{ item }}
    with_items:
      - python-setuptools
      - python-dev
      - build-essential
      - python-psycopg2
      - git
  - name: easy_install
    easy_install: name=pip
  - name: Descargar fuentes
    git: repo=https://github.com/AngelValera/bares-y-tapas-DAI dest=~/bares-y-tapas-DAI force=yes
  - name: Instalar requirements
    pip: requirements=~/bares-y-tapas-DAI/requirements.txt
```
* Además en el fichero [ansible_host](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/despliegueAzure/ansible_hosts) ponemos:

```
[localhost]
127.0.0.1              ansible_connection=local
```

* Hecho esto, podemos ejecutar:

```
vagrant up --provider=azure
```

Esto hace que se ejecute el vagrantfile. 

![](http://i666.photobucket.com/albums/vv21/angelvalera/Ejercicios%20tema%206/Seleccioacuten_002_zpsc3tsonux.png)

* Y vemos que también se ejecuta el playbook de ansible una vez creada la máquina virtual:

![](http://i666.photobucket.com/albums/vv21/angelvalera/Ejercicios%20tema%206/Seleccioacuten_003_zpsylr2hhzb.png)


* Ahora para desplegar la aplicación usamos **Fabric**, en un archivo [fabfile.py](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/fabfile.py).

```python
from fabric.api import task, run, local, hosts, cd, env
# Ejecutamos la aplicacion
def ejecutar_app():
    run('sudo  python /root/bares-y-tapas-DAI/manage.py runserver 0.0.0.0:80')
# Borramos la aplicacion
def borrar():
    run('sudo rm -r /root/bares-y-tapas-DAI')
# Realizar  Test
def test():
	run('sudo  python /root/bares-y-tapas-DAI/manage.py test ')
```
Para ejecutarlo tenemos que ejecutar:

```
sudo fab -p 'Clave#Angel#1' -H vagrant@maquinaavm2.cloudapp.net ejecutar_app
```

![](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/Seleccioacuten_011_zpscxuy4rvj.png)

* podemos comprobar que efectivamente funciona, [aplicación](http://maquinaavm2.cloudapp.net/):

![](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/Seleccioacuten_012_zps2ccmkcp0.png)

Todo se automatiza como he dicho en el siguiente [script](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/Scripts/azure.sh)