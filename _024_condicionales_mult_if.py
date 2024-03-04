# Pablo Darío Jiménez Nuño 21310143 practica_024_

print("Hola guerrero, ¿Que deseas comprar?╲n╲n" + "Items disponibles: ╲n╲n" + "espadas: ╲n╲n" + "espada nivel 1: 350 monedas de oro╲n" + "espada nivel 2: 1250 monedas de oro╲n" + "escudos: ╲n╲n" + "arco nivel 1: 120 monedas de oro╲n" + "arco nivel 2: 1000 monedas de oro╲n")

#en el anterior print lo unico que hacemos es dar una serie de avisos para que pueda entender el usuario de forma organizada con diferentes saltos de lineas entre otras cosas

comprar = [0]

#se declaran todas las posibles variablws que vayamos a ocupar en este caso son 5 dinero, espada1, espada2, arco1, arco2.
dinero=1500 
espadaLv1=350
espadaLv2=1250
arcoLv1=120
arcoLv2=1000

if 0 in comprar or comprar == []: #se coloca el numero 0 y abre toda la tienda y pide que escojas 1 numero entre el 1 al 4
    print("especifique un numero entre 1 y 4")

if 1 in comprar: #se escoje 1 y se cumple la condicion por lo que el programa sigue la primera condicion 
    dinero = dinero - espadaLv1 #se resta el valor del objeto al dinero que tenemos

if 2 in comprar: #se escoje 2 y se cumple la condicion por lo que el programa sigue la segunda condicion 
    dinero = dinero - espadaLv2 #se resta el valor del objeto al dinero que tenemos

if 3 in comprar: #se escoje 3 y se cumple la condicion por lo que el programa sigue la tercera condicion 
    dinero = dinero - arcoLv1 #se resta el valor del objeto al dinero que tenemos

if 4 in comprar: #se escoje 4 y se cumple la condicion por lo que el programa sigue la cuarta condicion 
    dinero = dinero - arcoLv2 #se resta el valor del objeto al dinero que tenemos

else: #en caso de que coloque un numero fuera del limite de 1-4
    print("que parte de 1 a 4 no entendiste? ajaja")

if dinero < 0: #cuando el marcador de dinero llega a menos de 0 se cumple esta condicion 
    print("EEEE me estorbas a los clientes ")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]: #si se cumple la condicion de que hayas comprado un objeto te da 2 notificaciones la cantidad de oro actual y los objetos en tu bolso
    print("Te quedan "+ str(dinero) + "monedas de oro")
    print("Se añadieron el/los objetos a tu inventario ")
