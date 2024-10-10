Algoritmo sin_titulo
	//Hacer un algoritmo para una heladería que tiene 4 tipos de empleados,
	//ordenados de la siguiente forma con su número identificador y salario diario correspondiente:
	// *Cajero (56$/día).
	// *Servidor (64$/día).
	// *Preparador de mezclas (80$/día).
	// *Mantenimiento (48$/día).
	//El dueño de la tienda desea tener un programa donde sólo ingrese dos números enteros que representen
	//al número identificador del empleado y la cantidad de días que trabajó en la semana (6 días máximos).
	//Y el programa le mostrará por pantalla la cantidad de dinero que el dueño le debe pagar al empleado que ingresó.
	
	Dimension escala_sueldo[5,7]
	
	Para i<-1 hasta 5
		Para j<-0 hasta 7 
			Mostrar "[", i*j "]" Sin Saltar
		FinPara
		Mostrar " ";
	FinPara
	
	Mostrar "Elija la categoria laboral 1 a 4"
	
FinAlgoritmo
