# Pablo Darío Jiménez Nuño 21310143 practica_041_

class Usuarios: # Definicien de la clase Usuarios (superclase)
    # Metodo especial __init__ que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre, edad): # Inicializacion de los atributos nombre y edad con los valores proporcionados
        self.nombre = nombre
        self.edad = edad

    def muestra_datos(self): # Metodo para mostrar los datos del usuario
        print("El nombre de usuario es: " + self.nombre + " y tiene: " + str(self.edad) + " años")

usuario1 = Usuarios("Pablo", 21) # Creacion de una instancia de Usuarios con nombre Pablo y edad 21
usuario1.muestra_datos()

class Usuarios_premium(Usuarios):
    # Metodo especial __init__ que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre, edad, instagram):# Inicializacion de los atributos nombre, edad y instagram con los valores proporcionados
        Usuarios.__init__(self, nombre, edad)
        self.instagram = instagram

    def muestra_datos_premium(self): # Metodo para mostrar los datos del usuario
        print("El nombre de usuario es: " + self.nombre + " y tiene: " + str(self.edad) + " y su instagram es: " + self.instagram)

usuario2 = Usuarios_premium("aldo", 23, "aldo.loba") # Creacion de una instancia de Usuarios con nombre aldo y edad 23 y instagram aldo.loba
usuario2.muestra_datos_premium()

