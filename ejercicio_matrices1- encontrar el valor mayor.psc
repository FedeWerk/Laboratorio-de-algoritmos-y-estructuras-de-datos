Algoritmo ejercicio_matricces
	//1) Solicitar a un usuario que ingrese valores para una matriz de 2 x 5 y determinar
	//cual fué el numero mayor mediante una búsqueda.
	
	Dimension MatrizA[2,5];
		
	Para i<-1 hasta 2 con paso 1 hacer
		Para j<-1 hasta 5 con paso 1 Hacer
			Escribir "Ingrese los numeros que conformaran los elementos de la matriz"
			Leer MatrizA[i,j]
		FinPara
	FinPara
	
	Escribir "La matriz es:"
	Para i<-1 Hasta 2 Con Paso 1 Hacer
		Para j<-1 Hasta 5 Con Paso 1 Hacer
			Escribir "[ ", MatrizA[i,j],"]" Sin Saltar;
		Fin Para
		Escribir " ";
	Fin Para
	
	Valor_mayor=MatrizA[1,1]
	Para i<-1 hasta 2 con paso 1 Hacer
		para j<-1 hasta 5 con paso 1 Hacer
			si MatrizA[i,j]>Valor_mayor
				Valor_mayor<-MatrizA[i,j]
			FinSi
		FinPara
	FinPara
	Escribir "El elemento mayor es: ", Valor_mayor
	
FinAlgoritmo
