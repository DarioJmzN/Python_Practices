# Pablo Darío Jiménez Nuño 21310143 practica_031_

teclado1 = { #se abre un nuevo diccionario llamado teclado1
	'Categoría': 'Teclados', #atributos del teclado1
	'Modelo': 'HyperX Alloy FPS Pro', #atributos del teclado1
	'Precio': '89,99' #atributos del teclado1
}

teclado2 = {  #se abre un nuevo diccionario llamado teclado2 
	'Categoría': 'Teclados', #atributos del teclado1
	'Modelo': 'Corsair K55 RGB', #atributos del teclado1
	'Precio': '59,99' #atributos del teclado1
}

for x in teclado2: #se va leer cada atributo general de x
	print(x)
	
print ("______________")

for z in teclado2: #se va a leer cada atributo particular de x
	print(teclado2[z])
	