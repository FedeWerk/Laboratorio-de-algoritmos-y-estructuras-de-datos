"Trabajo práctico evaluativo - Analisis de nombres"

def menu():
    print(" ")
    print("Selecciona una opción del menú:")
    print("1. Ingresar nombres.\n" 
        "2. Ver lista de nombres ingresados.\n"
        "3. Ordenar los nombres.\n"
        "4. Longitud de los nombres\n"
        "5. Cantidad de vocales y consonantes.\n"
        "6. Cantidad de palabras por nombres.\n"
        "7. Ver nombres invertidos.\n"
        "8. Nombres que empiezan con ...\n"
        "9. Buscar nombres en la lista\n"
        "10. Salir\n"
        " ")
    opcion=input("Opcion: ")
    print(" ")
    return opcion

lista_nombres=[]
nombres_minuscula=[]
opcion="1"

while opcion=="1" or opcion=="2" or opcion=="3" or opcion=="4" or opcion=="5" or opcion=="6" or opcion=="7" or opcion=="8" or opcion=="9" or opcion=="10":
    opcion=(menu())

    while opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4" and opcion!="5" and opcion!="6" and opcion!="7" and opcion!="8" and opcion!="9" and opcion!="10":
        print("Has ingresado una opción inválda.\nSelecciona nuevamente: ")
        opcion=(menu())

    if opcion=="1":
        print('Ingresa el nombre de cada estudiante: \n - Para finalizar la tarea escriba "fin". \n - Para ver los nombres que ha cargado escriba "repetir".')
        nombre=opcion

        while nombre != "Fin" and nombre !="Repetir":
            nombre=input()
            nombre=nombre.capitalize()
            if nombre.replace(" ","").isalpha()==False:
                print("(!) Ha ingresado un nombre invalido, pruebe nuevamente.")
            else:
                lista_nombres.append(nombre)
                nombres_minuscula.append(nombre.lower())
            
            if nombre == "Fin":
                print(">> Ingreso de nombres finalizado <<".center(10))
                lista_nombres.pop()
                nombres_minuscula.pop()
                            
            if nombre == "Repetir":
                lista_nombres.pop()
                nombres_minuscula.pop()
                for indice, nombre in (enumerate(lista_nombres)):
                    print(indice+1, nombre.capitalize())
                print(" ")
            
    elif lista_nombres == [] and opcion!="10":
        print("(!) No hay nombres cargados")

    elif opcion=="2":
        print("La lista actual de nombres ingresados es:")
        for indice, nombre in (enumerate(lista_nombres)):
            print(indice+1, nombre.capitalize())

    elif opcion=="3":
        nombres_ordenados=sorted(lista_nombres)
        print("La lista de nombres ordenada alfabéticamente es:")
        for indice,nombre in (enumerate(nombres_ordenados)):
            print(indice+1, nombre.capitalize())

    elif opcion=="4":
        long="1"
        short="10000000000000000000000000000"
        for name in nombres_minuscula:
            if len(name.replace(" ",""))>len(long):
                long=name
            elif len(name.replace(" ",""))<len(short):
                short=name
        print(f"El nombre más largo de la lista es '{long.capitalize()}', mientras que el nombre más corto es '{short.capitalize()}'")

    elif opcion=="5":
        cantidad_vocales=0
        for nombre in nombres_minuscula:
            cantidad_vocales=cantidad_vocales+nombre.replace(" ","").count("a")
            cantidad_vocales=cantidad_vocales+nombre.replace(" ","").count("e")
            cantidad_vocales=cantidad_vocales+nombre.replace(" ","").count("i")
            cantidad_vocales=cantidad_vocales+nombre.replace(" ","").count("o")
            cantidad_vocales=cantidad_vocales+nombre.replace(" ","").count("u")
        print(f"Entre todos los nombres hay {cantidad_vocales} vocales.")
        letras=0
        for nombre in nombres_minuscula:
            letras=letras+len(nombre.replace(" ",""))
        cantidad_consonantes=letras-cantidad_vocales
        print(f"Entre todos los nombres hay {cantidad_consonantes} consonantes.")
    
    elif opcion=="6":
        for nombre in nombres_minuscula:
            palabras_por_nombre=nombre.split()
            if len(palabras_por_nombre)==1:
                print(f"El nombre {nombre.capitalize()} tiene 1 palabra.")
            else:
                print(f"El nombre {nombre.capitalize()} tiene {len(palabras_por_nombre)} palabras.")

    elif opcion=="7":
        print(f"Si invertimos cada nombre, la lista quedaría:" )
        for nombre in lista_nombres:
            nombre.capitalize()
            print("-", nombre[::-1])

    elif opcion=="8":
        print("Elije una letra:")
        letra_inicio=input()
        letra_inicio=letra_inicio.lower()
        print(f"Los nombres que empiezan con {letra_inicio.upper()} son:")
        for nombre in nombres_minuscula:
            if nombre.startswith(letra_inicio):
                print("-", nombre.capitalize())
            
    elif opcion=="9":
        n=0
        busqueda=input("Escribe el nombre que quieres buscar: ")
        for nombre in nombres_minuscula:
            if nombre==busqueda.lower():
                print(f"- {busqueda.capitalize()} SI se encuentra en la lista.")
                break
            else:
                n=n+1
        
        if n==len(nombres_minuscula):
            print(f"- {busqueda.capitalize()} NO se encuentra en la lista.")

    elif opcion=="10":
        exit
        break

            


