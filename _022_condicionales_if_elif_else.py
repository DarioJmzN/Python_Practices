# Pablo Darío Jiménez Nuño 21310143 practica_022_ 

edad = int(input('¿Cuál es tu edad?\n')) #se declara una variable edad, y procede a pedir un numero entero y ese numero se guarda en edad
if edad <= 0: #se inicia la condicion if si ponen un valor menor a 0
	print('Nadie puede tener esa edad.') 
elif edad <= 1 and edad <= 17: # se llega aun limite de edad mientras sea mayor o igual a uno y menor o igual 18 si se cumple imprime el siguiente print 
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 100: #se tiene otra condicion si la edad es de 18 a 100 se imprime el siguiente print 
	print('Eres mayor de edad.')
else: #en caso de que ninguno de las condiciones anteriores se cumpla else hace efecto dando el siguiente print
	print('Edad no válida.')