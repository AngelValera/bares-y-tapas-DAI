##**Integración continua**##

Para la integración continua he utilizado travis, ya que es el que me ha resultado más sencillo de utilizar junto con github:

Para su uso debemos indicar el repositorio que queremos testear y además generar el fichero **[.travis.yml](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/requirements.txt)** donde se indican la versión de python usada, como instalar las dependencias y como pasar los test.

Para las dependencias se utiliza un fichero llamado **[requirements.txt](https://github.com/AngelValera/bares-y-tapas-DAI/blob/master/requirements.txt)** con lo necesario para ejecutar la aplicación.

Para generar la documentación, se utiliza la herramienta epydoc de la siguiente manera:

**Documentación:**

```
epydoc --html views.py models.py
```

Para ello debemos estar en el directorio de la aplicación, **app**.