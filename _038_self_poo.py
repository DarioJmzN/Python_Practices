# Pablo Darío Jiménez Nuño 21310143 practica_038_

# se  Definine la clase Usuario
class Usuario:
    # la palabra reservada para __init__ que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre, apellidos):
        # Inicializamos a los atributos nombre y apellidos con los valores que se nos proporcionam
        self.nombre = nombre
        self.apellidos = apellidos

    # Método que nos va a imprimir los datos del usuario
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Creación de una instancia de Usuario con nombre paco y apellidos Jimenez hernandez
usuario001 = Usuario('paco', 'Jimenez hernandez')

# Creación de otra instancia de Usuario con nombre cony y apellidos nuño sauza
usuario002 = Usuario('cony', 'nuño sauza')

# Cambio del atributo nombre de usuario002 a 'feliciano'
usuario002.nombre = 'feliciano'

# Llamada al método imprime_datos para mostrar los datos del usuario002
# Nota: Se imprimirá el nombre actualizado 'Jacinto' y los apellidos 'Gomila Reyes'
usuario002.imprime_datos()