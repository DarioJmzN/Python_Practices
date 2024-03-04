# Pablo Darío Jiménez Nuño 21310143 practica_036_

class Usuario: #se hace una clase llamada usuario
	nombre = '' #se le da el atributo nombre
	apellidos = '' #se le da el atributo apellido

	def imprime_datos(self): #se hace una funcion llamada imprime_datos 
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos) #imprimimos los datos requeridos

usuario001 = Usuario() #se llama a nuestra clase

usuario001.nombre = 'Osmin' #le asignamos al atributo nombre como= Osmin
usuario001.apellidos = 'fregozo angel' #le asignamos al atributo apellido como= fregozo angel

usuario001.imprime_datos() #se usa al usuario junto a la funcion para mostrarnos sus atributos