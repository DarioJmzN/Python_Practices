# Pablo Darío Jiménez Nuño 21310143 practica_048_

import re #importa la libreria re
texto = "El futuro es ahora." #define una string en una variable "una cadena de texto"
buscar = re.findall("pasado|futuro", texto)
if buscar: # Verifica si hay al menos una coincidencia en la lista obtenida
	print("Hay al menos una coincidencia.")
else: #lo que hace en caso de que no haya coincidencias
	print("No hay coincidencias.")