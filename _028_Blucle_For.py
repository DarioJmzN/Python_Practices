# Pablo Darío Jiménez Nuño 21310143 practica_028_

for x in 'Python': #python es un string por lo que va estar tomado cada letra el valor de x
    print(x) #imprime x

print( "____________ "   )

cursos = ['Python', 'JavaScript', 'COBOL', 'HTML'] #lista llamada cursos

for z in cursos: #lee la lista cursos
	if z == "COBOL": #se habre condicion si z es igual a COBOL entonces...
		break #cierra el ciclo for
	print(z) #imprime z

print( "____________ "   )

for z in cursos: #lee la lista cursos
	if z == "COBOL":  #se habre condicion si z es igual a COBOL entonces...
		continue #se salta a COBOL
	print(z) #imprime z
	
