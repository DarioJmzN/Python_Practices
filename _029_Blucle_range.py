# Pablo Darío Jiménez Nuño 21310143 practica_029_

for x in range(10): #range empieza a contar desde el 0 e incrementa de 1 en 1
	print(x) #imprime la variable x
	
print( "____________ "   )

for y in range(5,10): #da la condicion inicial 5 y se ejecuta hasta el 10
	print(y) #imprime la variable y
	
print( "____________ "   )

for z in range(10, -500, -50): #da la condicion inicial 10 y se ejecuta hasta el -500 y decrese de 50 en 50
	print(z) #imprime la variable z
	
print( "____________ "   )

print ("lista de numeros: \n")

numeros = [2,4,8,16,32,64,128] #lista de valores numericos

for c in range(len(numeros)): #range empieza a contar desde la posicion 0 de la lista
	print("numero de la operacion -> ", c, "multiplicacion -> ", numeros[c], "resultado -> ", numeros[c] * numeros[c]) #imprime un mensaje y hace operaciones aritmeticas 