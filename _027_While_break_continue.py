# Pablo Darío Jiménez Nuño 21310143 practica_027_

x = 1 #variable entera 

while x <= 10: #se va a ser un ciclo while en el que si x es menor o igual a 10 se va a cumplir 
	print(x) #se imprime el valor de x
	if x == 5: #se pone una condicion para x igual a 5 
		break #se cumplio la condicion y break rompe el flujo de ejecucion del while
	x += 1 #incremento de x de 1 en 1
	
z = 0 #variable entera 

while z < 10: #se abre cilo while para cuando z es menor a 10
	z += 1 #incremento de z de 1 en 1
	if z == 5 or z == 7: #condicion si z vale 5 o 7 se va a cumplir la condicion y va a pasar al continue que lo va a saltar
		continue #declaracion de "salto"
	print(z) #imprime z