# Pablo Darío Jiménez Nuño 21310143 practica_047_

import re #importa la libreria llamada re

texto = "tres tristes tigres comen trigo en un trigal" #se guarda en la variable texto un string
busqueda = re.findall("e", texto) #buscar todas las ocurrencias de un patrón dentro de una cadena y devolver una lista con todas las coincidencias encontradas.
print(busqueda) #se imprime la variable busqueda