# Pablo Darío Jiménez Nuño 21310143 practica_023_

#navegadores = ['chrome', 'firefox', 'opera', 'safari']
# print('chrome' in navegadores) #se comprueba si chrome se encuentra en la lista navegadores y manda un True o false segun sea el caso

entrada = input('Introduce el nombre de un navegador:\n') #se pide un dato y se guarda en la variable entrada
navegadores = ['chrome', 'firefox', 'opera', 'safari'] # una lista llamada navegadores con 4 tipos de navegadores
if entrada in navegadores: #exite una condicion de comprovacion si entrada se encuentra en la lista imprime el mensaje de if
	print('El navegador que buscas está en la lista.')
else: #en caso de que no se cumpla las condiciones manda el siguiente print
	print('El navegador que buscas no está en la lista.')