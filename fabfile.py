from fabric.api import task, run, local, hosts, cd, env


#  Ejecutamos la aplicacion
def ejecutar_app():
    run('sudo  python /root/bares-y-tapas-DAI/manage.py runserver 0.0.0.0:80 &')

#  Borramos la aplicacion
def borrar():
    run('sudo rm -r /root/bares-y-tapas-DAI')

# Realizar  Test
def test():
	run('sudo  python /root/bares-y-tapas-DAI/manage.py test ')
