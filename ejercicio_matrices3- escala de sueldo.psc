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
		
	Dimension sueldo[4,1]
	sueldo(1,1)=56
	sueldo(2,1)=64
	sueldo(3,1)=80
	sueldo(4,1)=48
		
	Mostrar "Elija la categoria laboral:"
	Mostrar "1. Cajero"
	Mostrar "2. Servidor"
	Mostrar "3. Preparador de mezclas"
	Mostrar "4. Mantenimiento."
	Leer categoria
	
	dias=0
	mientras dias<1 o dias>6 Hacer
		Mostrar "Ingrese la cantidad de d�as trabajados esta semana (1 a 6 d�as)"
		Leer dias
	FinMientras
		Mostrar "EL empleado debe cobrar $" sueldo(categoria,1)*dias
	
FinAlgoritmo
