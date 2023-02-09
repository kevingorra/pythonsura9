import pandas as pd

tablaempleados=pd.read_csv('./datos/empleados.csv')
print(tablaempleados)


tablanalistas1=tablaempleados[tablaempleados['cargo']=='analista1'].head(50)

archivohtml=tablanalistas1.to_html()
archivotexto=open('datoanalaistas1.html','w')
archivotexto.write(archivohtml)
archivotexto.close()