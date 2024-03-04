# Pablo Darío Jiménez Nuño 21310143 practica_032_

teclado1 = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print(len(teclado1) + len(teclado2))

# del teclado1['Precio'] #puedomos borrar un diccionario completo con del aun que aqui solo eliminamos a precio del teclado1
# print(teclado1)
vistateclado = teclado1.keys() #llama a los atrivutos sin sus valores 
print(vistateclado) #imprime los atributos de teclado1 

teclado1['Color'] = 'Negro' #agregamos al diccionario de teclado 1 el atrivuto color --> Negro
print(teclado1) #imprime teclado1

teclado2['Color'] = 'Azul'  #agregamos al diccionario de teclado 2 el atrivuto color --> Azul
print(teclado2) #imprime teclado2