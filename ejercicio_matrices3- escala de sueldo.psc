Algoritmo sin_titulo
	//Hacer un algoritmo para una helader�a que tiene 4 tipos de empleados,
	//ordenados de la siguiente forma con su n�mero identificador y salario diario correspondiente:
	// *Cajero (56$/d�a).
	// *Servidor (64$/d�a).
	// *Preparador de mezclas (80$/d�a).
	// *Mantenimiento (48$/d�a).
	//El due�o de la tienda desea tener un programa donde s�lo ingrese dos n�meros enteros que representen
	//al n�mero identificador del empleado y la cantidad de d�as que trabaj� en la semana (6 d�as m�ximos).
	//Y el programa le mostrar� por pantalla la cantidad de dinero que el due�o le debe pagar al empleado que ingres�.
	
	Dimension escala_sueldo[5,7]
	
	Para i<-1 hasta 5
		Para j<-0 hasta 7 
			Mostrar "[", i*j "]" Sin Saltar
		FinPara
		Mostrar " ";
	FinPara
	
	Mostrar "Elija la categoria laboral 1 a 4"
	
FinAlgoritmo
