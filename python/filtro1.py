import matplotlib.pyplot as plt
from cargarDatos import cargarDatos


def filtroMedellin():
    tabla=cargarDatos()
    filtro=tabla[tabla["Ciudad"]=="Caucasia"]
    filtro=filtro.loc[:,["Vereda","Arboles"]]
    filtro=filtro.set_index("Vereda")
    filtro = filtro.groupby("Vereda").agg(sum)
    filtro.plot(kind = 'bar', color='#FFD700')

    #plt.plot(filtro["Vereda"],filtro["Arboles"])
    plt.show()
    #return filtro
    #tabla = pd.read_csv("./datos/Siembras.csv",index_col="Ciudad").tail(10)
    #tabla["Arboles"].plot(kind = 'bar')

filtroMedellin()