Algoritmo parcial_Algoritmos
	//VECTORES
	//Derrollar un programa que solicite una cantidad de n�meros determinada por el usuario los cuales ser�n evaluados para determinar:(4 puntos)
	//- El mayor
	//- El menor
	//- La cantidad de n�meros ingresados mayores que 5.
	//- La suma de todos los n�meros.
	
	Mostrar "Elija la cantidad m�xima de n�meros que se podr�n ingresar en el listado:"
	Leer n
	Dimension listado[n]
	
	Mostrar "Ingrese cada n�mero:"
	Para i<-1 hasta n Hacer
		Leer dato
		listado[i]=dato
	FinPara
	
	Mostrar "El listado de n�meros es: "
	Para i<-1 hasta n Hacer
		Mostrar "-" listado[i]
	FinPara
	
	num_mayor=0
	Para i<-1 hasta n Hacer
		si listado[i]>num_mayor 
			num_mayor=listado[i]
		FinSi
	FinPara
	Mostrar "El n�mero m�s grande de la lista es: " num_mayor
	
	num_menor=num_mayor
	Para i<-1 hasta n Hacer
		si listado[i]<num_menor
			num_menor=listado[i]
		FinSi
	FinPara
	Mostrar "El n�mero m�s chico de la lista es: " num_menor
	
	num_5=0
	m=0
	contador_vector=0
	Dimension listado_2[n]
	Para i<-1 hasta n Hacer
		si listado[i]>5 
			num_5=num_5+1
			para j<-1 hasta n Hacer
				listado_2[i]=listado[i]
			FinPara
		SiNo
			contador_vector=contador_vector+1
		FinSi
	FinPara
	
	Si contador_vector==n
		Mostrar "No hay n�meros mayores a 5."
	SiNo
		Mostrar "En la lista hay " num_5 " n�meros mayores a 5."
		Mostrar "Los n�meros mayores a 5 son :"
		Para i<-1 hasta n Hacer
			si listado_2[i]>5
				Mostrar "> " listado_2[i]
			FinSi
		FinPara
	FinSI
	
	suma_valores=0
	Para i<-1 hasta n Hacer
		suma_valores=suma_valores+listado[i]
	FinPara
	Mostrar "La suma de todos los valores del listado es: " suma_valores
	
	
	//MATRICES 
	
	//1) Crear una aplicaci�n que permita al usuario realizar carga  y  b�squeda de datos de la siguiente manera. 2 x 5. (6 puntos) 
	//Banana 3
	//Manzana 4
	//Pera 5
	//Kiwi 5
	//Melon 3
	
	//0 - Ingresar un articulo (frutas)
	//1 - Buscar un art�culo, IMPRIMIRLO 
	//2 - Imprimir todos los art�culos que fueron cargados previamente
	
	Dimension matriz[5,2]
	
	Mostrar "Ingresa cada producto: "
	Para i<-1 hasta 5 Hacer
		Para j<-1 hasta 1 Hacer
			Leer matriz[i,j]
		FinPara
	FinPara
	
	Mostrar "Ingresa la cantidad de cada producto: "
	Para i<-1 hasta 5 Hacer
		Para j<-2 hasta 2 Hacer
			Mostrar matriz[i,1] " " Sin Saltar
			Leer matriz[i,j]
		FinPara
	FinPara
	
	Para i<-1 hasta 5 Hacer
		Para j<-1 hasta 2 Hacer
			Mostrar " " matriz[i,j] " " Sin Saltar
		FinPara
		Mostrar " "
	FinPara
	
	Mostrar "�Desea buscar un art�culo?"
	Leer producto
	producto=Minusculas(producto)
	contador=0
	Para i<-1 hasta 5 Hacer
		Para j<-1 hasta 1 Hacer
			fruta=Minusculas(matriz[i,j])
			si producto == fruta
				Mostrar "En la lista HAY " matriz[i,2] " unidades de " producto
			SiNo
				contador=contador+1
			FinSi
		FinPara
	FinPara
	si contador==5
		Mostrar "NO hay " producto " en la lista."
	FinSi

	
FinAlgoritmo
