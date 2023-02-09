import pandas as pd

def cargarDatos():
    tabla = pd.read_csv("./datos/Siembras.csv")
    return(tabla)


