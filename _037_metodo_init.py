# Pablo Darío Jiménez Nuño 21310143 practica_037_

class Usuario: #se inicialisa nuestra clase usuario 
    def __init__(self, nombre, apellidos): # __init__ inicializar los atributos de un objeto
        self.nombre = nombre 
        self.apellidos = apellidos

    def imprime_datos(self):  #tenemos nuestra segunda funcion 
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Osmin', 'fregozo angel') #primer usuario con el nombre y apellido

usuario002 = Usuario('Paloma', 'Jimenez Nuño') #segundo usuario con el nombre y apellido

usuario001.imprime_datos() #tenemos a nuestra primera clase haciendo uso de las funcion de imprimir datos 
usuario002.imprime_datos() #tenemos a nuestra segunda clase haciendo uso de las funcion de imprimir datos 