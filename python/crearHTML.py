def crearHTML(tabla,nombre):

    html=tabla.to_html()
    archivo=open(nombre,"w")
    archivo.write(html)
    archivo.close()
