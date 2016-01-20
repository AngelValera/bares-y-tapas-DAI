import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_DAI.settings')

import django
django.setup()

from app.models import Bar, Tapa


def populate():
    bar1= add_bar('Bar1','DireccionBar1')

    add_tapa(bar=bar1,nombre="tapa1 bar1",descripcion="descripcion de la tapa 1")

    add_tapa(bar=bar1,nombre="tapa2 bar1",descripcion="descripcion de la tapa 2")

    add_tapa(bar=bar1,nombre="tapa3 bar1",descripcion="descripcion de la tapa 3")

    add_tapa(bar=bar1,nombre="tapa4 bar1",descripcion="descripcion de la tapa 4")


    bar2= add_bar('Bar2','DireccionBar2')

    add_tapa(bar=bar2,nombre="tapa1 bar2",descripcion="descripcion de la tapa 1")

    add_tapa(bar=bar2,nombre="tapa2 bar2",descripcion="descripcion de la tapa 2")

    add_tapa(bar=bar2,nombre="tapa3 bar2",descripcion="descripcion de la tapa 3")


    bar3= add_bar('Bar3','DireccionBar3')

    add_tapa(bar=bar3,nombre="tapa1 bar3",descripcion="descripcion de la tapa 1")

    add_tapa(bar=bar3,nombre="tapa2 bar3",descripcion="descripcion de la tapa 2")


    # Print out what we have added to the user.
    for b in Bar.objects.all():
        for t in Tapa.objects.filter(bar=b):
            print "- {0} - {1}".format(str(b), str(t))

def add_tapa(bar, nombre, descripcion, votos=0):
    tapa = Tapa.objects.get_or_create(bar=bar, nombre=nombre)[0]
    tapa.votos=votos
    tapa.descripcion=descripcion
    tapa.save()
    return tapa

def add_bar(nombre, direccion, visitas=0):
    bar = Bar.objects.get_or_create(nombre=nombre)[0]
    bar.direccion= direccion
    bar.visitas=visitas
    bar.save()
    return bar

# Start execution here!
if __name__ == '__main__':
    print "Starting App population script..."
    populate()
