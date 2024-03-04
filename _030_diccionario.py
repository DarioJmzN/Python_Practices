# Pablo Darío Jiménez Nuño 21310143 practica_030_

teclado1 = {  #lo interesante de los diccionarios es que podemos tener atributos y con esto nos metemos en el paradigma de orientado a objetos
	'Categoría': 'Teclados', #atributos del teclado1
	'Modelo': 'HyperX Alloy FPS Pro', #atributos del teclado1
	'Precio': '89,99' #atributos del teclado1
}

teclado2 = { #se abre un nuevo diccionario llamado teclado2 
	'Categoría': 'Teclados', #atributos del teclado2
	'Modelo': 'Corsair K55 RGB', #atributos del teclado2
	'Precio': '59,99'#atributos del teclado2
}

consulta = teclado1['Modelo'], teclado1["Precio"], teclado2['Modelo'], teclado2['Precio'] #en esta parte la entendi por llamas al objeto y justo despues el atributo el cual quieres saber que es
print(consulta) #imprime nuestra variable consulta que contiene todos atributos de los 2 diccionarios