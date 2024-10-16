Algoritmo tablas_multiplicar
	
	Dimension tabla[10]
	num=0
	
	Mostrar "Ingrese un número para ver su tabla de multiplicar desde el 1 hasta el 10."
	Leer  num
	
	para i<-1 hasta 10 Hacer
		tabla[i] <- i*num
	FinPara
	Mostrar "La tabla de " num	" del 1 al 10 es:"
	para i<-1 hasta 10 Hacer
		Mostrar tabla[i]
	FinPara
	
	
FinAlgoritmo
