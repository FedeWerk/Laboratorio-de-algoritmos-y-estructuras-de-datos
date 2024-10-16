Algoritmo ejericios
	//EJERCICIO 1
	dimension cedula[10]
	dimension nombre[10]
	Para i<-1 Hasta 10 Hacer
		Escribir "ingrese su nombre"
		Leer nombre[i]
		Escribir "ingrese su cedula"
		Leer cedula[i]
	FinPara
	Para i<-1 Hasta 10 Hacer
		Escribir "ingrese su nombre",nombre[i]
		Escribir "ingrese su cedula",cedula[i]
	FinPara
	
	//EJERCIOCIO 2
	Dimension cedula[10]
	Dimension nombre[10]
	Para i<-1 Hasta 10 Hacer
		Escribir 'ingrese su nombre'
		Leer nombre[i]
		Escribir 'ingrese su cedula'
		Leer cedula[i]
	FinPara
	Escribir 'ingreese su cedula para ver si esta en el programa'
	Leer c
	Para i<-1 Hasta 10 Hacer
		Si c=cedula(i) Entonces
			Escribir 'si,corresponde a ", nombre(i)
			i = 10
		FinSi
	FinPara
	
	//EJERICIO 3
	Escribir 'ingresa la cantidad de numeros'
	Leer n
	Dimension A[n]
	Dimension B[n]
	Dimension C[n]
	Para i<-1 Hasta n Hacer
		Escribir 'ingrese ', i ,' numero'
		Leer A[i]
		Si A[i] MOD 3=0 Entonces
			B[i] <- A[i]
			multiplos <- multiplos+1
		FinSi
		Si A[i] MOD 2=1 Entonces
			C[i] <- A[i]
			impares <- impares+1
		FinSi
	FinPara
	Escribir 'la cantidad de numeros impares son ',impares
	Para l<-1 Hasta n Hacer
		Si C[l]<>0 Entonces
			Escribir C[l]
		FinSi
	FinPara
	Escribir 'la cantidad de multiplos de 3 son ', multiplos
	Para j<-1 Hasta n Hacer
		Si B[j]<>0 Entonces
			Escribir B[j]
		FinSi
	FinPara
	Escribir "estos son todos los numeros ingresados"
	Para f<-1 Hasta n Hacer
		Escribir A[f]
	FinPara
	
	//EJERCICIO 4
	
	may <- 0
	Dimensionar l(20,3)
	Para f<-1 Hasta 20 Con Paso 1 Hacer
		l[f,1]<-aleatorio(0,100)
		l[f,2]<-l[f,1]
	FinPara
	cont = 0
	Para i<-20 Hasta 1 Con Paso -1 Hacer
		Para i1<-1 Hasta 20 Con Paso 1 Hacer
			Si may<l[i1,2] Entonces
				may = l[i1,2]
			FinSi
		FinPara
		l[i,3]<-may
		Para v<-1 Hasta 20 Hacer
			Si l[i,3]=l[v,2] Entonces
				l[v,2]=0
				v = 20
			FinSi
		FinPara
		may = 0
	FinPara
	Escribir "La lista de los numeros aleatorios son:"
	Para i<-1 Hasta 20 Con Paso 1 Hacer
		Escribir l[i,1]
	FinPara
	Escribir "La lista de los numeros ordenados del menor al mayor son:"
	Para i<-1 Hasta 20 Con Paso 1 Hacer
		Escribir l[i,3]
	FinPara
	
FinAlgoritmo


