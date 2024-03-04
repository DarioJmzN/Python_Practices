# Pablo Darío Jiménez Nuño 21310143 practica_045_

import datetime, locale  #Importa las librerias datetime y locale

locale.setlocale(locale.LC_ALL, "es-ES") #las fechas y horas serán formateadas según las convenciones locales de España

fecha = datetime.datetime.now() #Utiliza el método strftime() del objeto datetime para formatear la fecha y hora según un formato específico. 

print(fecha.strftime("%A")) # En este caso, se pasa "%A" como argumento, que representa el nombre completo del día de la semana.