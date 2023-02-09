from cargarDatos import cargarDatos
from crearHTML import crearHTML


def filtroMedallo():

    tabla=cargarDatos()
    tablaMedallo=tabla[tabla["Ciudad"]=="Barbosa"]

    return tablaMedallo

filtro=filtroMedallo()
crearHTML(filtro,"prueba.html")

