# Pablo Darío Jiménez Nuño 21310143 practica_049_

variable = "Correcto." #variable que contiene un string "correcto"

try: # Se utiliza un bloque try-except para manejar posibles excepciones
	print(variable) #imprime el valor de variable
except: # Si ocurre una excepción durante la impresión, se imprime un mensaje indicando que la variable no está declarada
	print("La variable no está declarada.") #imprime un texto