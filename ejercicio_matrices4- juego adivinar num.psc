Algoritmo ejercicio_4
	//4) Elaborar un juego que permita al usuario ingresar un n�mero. 
	//El programa buscar� un numero al azar y comparar� los mismos.
	//En caso de que sean iguales el usuario acert� por lo que tendr� 10 tiros mas.
	//En caso de que no sean iguales descontaremos un tiro.
	//El total de tiros al comienzo es de 5.
	//Deberemos comunicar cada acierto, desacierto y la cantidad de tiros.
	//Implementar un sistema de puntaje
	
	Mostrar "�Vamos a jugar! Tendr�s 5 oportunidades para adivinar un n�mero entre 0 y 10."
	Mostrar "�Si aciertas tendr�s 10 oportunidades m�s!"
	Mostrar "�CUIDADO! SI fallas perderas un oportunidad"
	
	tiros=5; puntos=0
	Mientras tiros>0 Hacer
		random	= Aleatorio(0,11)
		Mostrar "Elige un n�mero:"
		Leer eleccion
		si eleccion == random
			Mostrar "�Acertaste! �Sumaste 10 puntos y 10 oportunidades m�s!"
			puntos=puntos+10
			tiros=tiros+9
		SiNo
			Mostrar "�Fallaste! :( Perdiste 1 oportunidad." 
			tiros=tiros-1
		FinSi
		Mostrar "Tu elecci�n era " eleccion ". El n�mero correcto era " random
		Mostrar "Tienes " puntos " puntos y " tiros " oportunidades."
	FinMientras
	Mostrar "En total obtuviste " puntos " puntos."
	
FinAlgoritmo

