# Pablo Darío Jiménez Nuño 21310143 practica_040_



class Usuarios: # Definicien de la clase Usuarios (superclase)
    # Metodo especial __init__ que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre, edad): # Inicializacion de los atributos nombre y edad con los valores proporcionados
        self.nombre = nombre
        self.edad = edad

    # Metodo para mostrar los datos del usuario
    def muestra_datos(self): # Imprime el nombre y la edad del usuario
        print('El nombre del usuario es:', self.nombre, '\nTiene:', self.edad)

usuario1 = Usuarios("leah", 35) # Creacion de una instancia de Usuarios con nombre leah y edad 35

usuario1.muestra_datos() # Llamada al metodo muestra_datos para mostrar los datos de usuario1

class UsuariosPremium(Usuarios): # Definicion de la subclase UsuariosPremium que hereda de Usuarios
    pass  # No se define ningún metodo especifico, hereda todos los métodos de la clase Usuarios

# Creación de una instancia de UsuariosPremium con nombre deadlock y edad 32
usuario2 = UsuariosPremium("deadlock", 32)
usuario2.muestra_datos()