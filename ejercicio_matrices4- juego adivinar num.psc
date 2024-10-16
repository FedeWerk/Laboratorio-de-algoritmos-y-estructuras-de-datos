Algoritmo ejercicio_4
	//4) Elaborar un juego que permita al usuario ingresar un número. 
	//El programa buscará un numero al azar y comparará los mismos.
	//En caso de que sean iguales el usuario acertó por lo que tendrá 10 tiros mas.
	//En caso de que no sean iguales descontaremos un tiro.
	//El total de tiros al comienzo es de 5.
	//Deberemos comunicar cada acierto, desacierto y la cantidad de tiros.
	//Implementar un sistema de puntaje
	
	Mostrar "¡Vamos a jugar! Tendrás 5 oportunidades para adivinar un número entre 0 y 10."
	Mostrar "¡Si aciertas tendrás 10 oportunidades más!"
	Mostrar "¡CUIDADO! SI fallas perderas un oportunidad"
	
	tiros=5; puntos=0
	Mientras tiros>0 Hacer
		random	= Aleatorio(0,11)
		Mostrar "Elige un número:"
		Leer eleccion
		si eleccion == random
			Mostrar "¡Acertaste! ¡Sumaste 10 puntos y 10 oportunidades más!"
			puntos=puntos+10
			tiros=tiros+9
		SiNo
			Mostrar "¡Fallaste! :( Perdiste 1 oportunidad." 
			tiros=tiros-1
		FinSi
		Mostrar "Tu elección era " eleccion ". El número correcto era " random
		Mostrar "Tienes " puntos " puntos y " tiros " oportunidades."
	FinMientras
	Mostrar "En total obtuviste " puntos " puntos."
	
FinAlgoritmo

