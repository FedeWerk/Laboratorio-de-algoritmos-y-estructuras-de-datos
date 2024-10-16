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
		Mostrar "Ingrese la cantidad de días trabajados esta semana (1 a 6 días)"
		Leer dias
	FinMientras
		Mostrar "EL empleado debe cobrar $" sueldo(categoria,1)*dias
	
FinAlgoritmo
