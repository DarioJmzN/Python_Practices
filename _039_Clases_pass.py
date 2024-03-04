# Pablo Darío Jiménez Nuño 21310143 practica_039_

# Definición de la clase Usuarios
class Usuarios:
    # Método especial __init__ que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre, edad):
        # Inicializamos  los atributos "nombre y edad" con los valores proporcionados
        self.nombre = nombre
        self.edad = edad

    # es el metodo para mostrar los datos del usuario
    def muestra_datos(self):
        # se Imprime el nombre y la edad del usuario
        print("El nombre de usuario es:", self.nombre, "y su edad es:", self.edad)

# Creación de una instancia de Usuarios con nombre Fernando y edad 54
usuario1 = Usuarios("Fernando", 54)

# se Imprime el nombre y la edad de la instancia usuario1
print(usuario1.nombre, usuario1.edad)

# se Elimina la instancia usuario1
del usuario1

