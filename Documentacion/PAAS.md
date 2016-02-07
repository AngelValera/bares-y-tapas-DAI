##**Despliegue en un Paas Heroku**##
El siguiente paso es desplegar nuestra aplicación en un Paas, he utilizado heroku, lo he escogido porque aprendí a utilizarlo con los ejercicios del tema 3 y me resultó sencillo de usar, además de porque necesita un fichero de configuración que describe la infraestructura virtual.

La aplicación podemos verla funcionando [aquí](http://appbaresytapas.herokuapp.com/).

Por tanto los ficheros que necesitamos para el despliegue son:

- **Procfile:** se usa para que heroku sepa que tiene que ejecutar, para ello utiliza gunicorn:

```
web: gunicorn Proyecto_Merka.wsgi --log-file -
```
- **requirements.txt**: Como ya indiqué anteriormente para que la aplicación funcione necesita indicar que necesita para ejecutarse:

Una vez definidos estos ficheros debemos desplegarla en heroku, para ello hay que realizar una serie de comandos:

Lo primero es clonarnos el repositorio de github de la aplicación (si no lo teniamos ya clonado) y acontinuación:

**wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh**

**heroku login**-->Nos logueamos dentro de heroku

**heroku create**-->Creamos la aplicación dentro deheroku

**heroku apps:rename merka**-->Le cambiamos el nombre que nos pone por defecto por el de merka

**git push heroku master**-->La desplegamos.

En cuanto a la base de datos estoy usando la base de datos Postgresql que nos proporciona Heroku, en local sigo usando SQLite, para ello :

1- Instalar psycopg2.

2- Instalar dj_database_url.

3- Ahora en el fichero [setting.py](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/proyecto_DAI/settings.py) debemos añadir lo siguiente para poder usar SQLite en local y Postgree en Heroku:

```python
import dj_database_url
ON_HEROKU = os.environ.get('PORT')
if ON_HEROKU:
	DATABASE_URL='postgres://tnvbvmmuroapil:Myi9_1JBJZSP6EzjtEWN7Q9Arh@ec2-54-204-5-56.compute-1.amazonaws.com:5432/dfoub80thb1lb4'
	DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
```
Ahora debemos subir cambios a github y hacer git push heroku master y crear las tablas dentro de la base de datos para ello tenemos que introducir:

**1- heroku run python manage.py makemigrations**

**2- heroku run python manage.py migrate**

Los siguientes dos pasos no son obligatorios, yo los realizo para introducir directamente algunos bares y tapas a la aplicación, podemos ver el script [aquí](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/populate_app.py)

*3- heroku run python populate_app.py*

*4- heroku run python manage.py migrate*

**5- heroku run python manage.py createsuperuser**


Hecho esto, ya tenemos la aplicación desplegada.

Ahora añadimos integracion continua con Snap-ci, para ello seleccionamos el repositorio que queremos y lo configuramos de la siguiente manera:

![](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/Seleccioacuten_006_zpsx2snim1y.png)

![](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/Seleccioacuten_007_zpswkliblre.png)

![](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/Seleccioacuten_008_zpsis7kp5oy.png)

con esto cada vez que hagamos push  nos pasará los test y si son satisfactorios desplegará la aplicación.

##**Carpeta static con debug=False**

Cuando en el settings.py de nuestro proyecto indicamos:

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
```
Para que nos siga sirviendo el contenido estático, he realizado lo siguiente:

**En [settings.py](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/proyecto_DAI/settings.py):**

```python
ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
```

**En [urls.py](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/proyecto_DAI/urls.py):**

```python
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
```

Y para usar bootstrap, he usado un **cdn**  en el template [base.html](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/templates/app/base.html):

```
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" type="text/css">
```

![](http://i666.photobucket.com/albums/vv21/angelvalera/Proyecto%20final/Seleccioacuten_009_zpsrgdzbmdm.png)
