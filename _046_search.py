# Pablo Darío Jiménez Nuño 21310143 practica_046_

import re #importa la libreria re

texto = "Bienvenidos a Programación fácil" #se guarda un string en un variable llamada texto
busqueda = re.search("i", texto) # re.search buscar un patrón dentro de una cadena en este caso en texto
print(busqueda) #se imprime busqueda