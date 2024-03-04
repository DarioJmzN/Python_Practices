# Pablo Darío Jiménez Nuño 21310143 practica_034_

def alumnos_profesores(profesor, sustituto, *args): #se hace nuestra funcion alumnos profesores en el que cada que lo llamamos nos ca a poner el texto profesor: ___ sustituto: ___
    print("profesor: " + profesor) #se imprime profesor: + el nombre del profesor 
    print("sustituto: " + sustituto) #se imprime sustituto: + el nombre del sustituto 
    for x in args: #se inicia un ciclo for para que se repita la cantidad de veces que sea necesaria 
        print("alumno: " + x)

lista_alumnos=["andres", "ana", "pablo", "aldo"] #se hace una lista de alumnos que tiene a 4 andres, ana, pablo, aldo
alumnos_profesores("antonio", "amador", *lista_alumnos) #se llama la funcion y se le da los datos de el profesor antonio y el sustituto amador