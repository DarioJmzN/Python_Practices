# Pablo Darío Jiménez Nuño 21310143 practica_043_

import math #se importa la libreria math


def area(radio): # Define una función llamada area que calcula el área de un círculo
    # Calcula el area del circulo utilizando la formula: π * radio^2
    resultado = round(math.pi * radio * radio, 2)  # Round() redondea el resultado a 2 decimales
    print(resultado)  # Imprime el resultado del calculo

area(2) # Llama a la funcion 'area' con un radio de 2

# Define una funcion lambda llamada area que tambien calcula el area de un circulo
area = lambda radio: round(math.pi * radio * radio, 2)  # La funcion lambda tiene un solo parametro radio

print(area(2)) # Imprime el resultado de llamar a la funcion lambda area con un radio de 2