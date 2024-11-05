# Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
# la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
# cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
# estas opciones que tenemos aquí:
# 1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
# el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
# 2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
# escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
# a crear ese archivo en el lugar correcto.
# 3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
# una carpeta nueva con ese nombre.
# 4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
# a eliminar
# 5. La opción 5, le va a preguntar qué categoría quiere eliminar
# 6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.

import os
from pathlib import *
from os import system
path_base=os.path.abspath("Recetas")

def bienvenida():
    path_base=os.path.abspath("Recetas")
    print("\n¡BIENVENIDO!")
    print(f'''La ruta de acceso al directorio de recetas es:
    >>> {path_base} <<<''')
    nombre_de_categorias=os.listdir("Recetas")
    cantidad_categorias=len(nombre_de_categorias)
    print(f"\nActualmente hay {cantidad_categorias} categorías de recetas.")
    
#################### CONTAR RECETAS POR CATEGORIA ####################
    path_base=os.path.abspath("Recetas")
    nombre_de_categorias=os.listdir("Recetas")
    for i in nombre_de_categorias:
        categoria=i
        nombres_recetas=Path(path_base,categoria)
        listado_recetas=os.listdir(nombres_recetas)
        cantidad_recetas=len(listado_recetas)
        print(f"En la carpeta {i} hay {cantidad_recetas} recetas.")

#################### MOSTRAR RECETAS ####################
def mostrar_recetas():
    path_base=os.path.abspath("Recetas")
    
    print("Elije qué categoría te gustaría leer:")
    nombre_de_categorias=os.listdir("Recetas")
    
    #mostrar categorias
    for nombre in nombre_de_categorias:
        categoria=nombre
        print("-",categoria)
    #elegir categoria
    existe=True
    while existe==True:
        eleccion_categoria=input("Escribe el nombre de la opción que te interesa:")
        eleccion_categoria=eleccion_categoria.lower().capitalize()
        recetas_por_categoria=Path(path_base,eleccion_categoria)
        while recetas_por_categoria.exists()==False:
            system("cls")
            print("No existe esta categoría, ingresa nuevamente.")
            #mostrar categorias
            for nombre in nombre_de_categorias:
                categoria=nombre
                print("-",categoria)
            eleccion_categoria=input("Escribe el nombre de la opción que te interesa:")
            recetas_por_categoria=Path(path_base,eleccion_categoria)
                    
        nombres_recetas=os.listdir(recetas_por_categoria)
        print("\nLas recetas disponibles son:")
        for i,nombre in enumerate(nombres_recetas):
            receta=nombre
            print(i+1,")", receta)
        #elegir receta
        eleccion_receta=int(input("Ingresa el número de la receta que quieres preparar: "))
        receta_elegida=nombres_recetas[eleccion_receta-1]
        abrir_receta=Path(path_base,eleccion_categoria,receta_elegida)
        system("cls")
        print(abrir_receta.read_text())
        existe=False  
    

#################### ELIMINAR RECETAS ####################
def eliminar_receta():
    path_base=os.path.abspath("Recetas")
    
    print("Elije de qué categoría te gustaría eliminar una receta:")
    nombre_de_categorias=os.listdir("Recetas")
    
    #mostrar categorias
    for nombre in nombre_de_categorias:
        categoria=nombre
        print("-",categoria)
    #elegir categoria
    existe=True
    while existe==True:
        eleccion_categoria=input("Escribe el nombre de la categoría que te interesa:")
        eleccion_categoria=eleccion_categoria.lower().capitalize()
        recetas_por_categoria=Path(path_base,eleccion_categoria)
        if recetas_por_categoria.exists()==False:
            print("No existe esta categoría, ingresa nuevamente.")
            eleccion_categoria=input("Escribe el nombre de la categoría que te interesa:")
        else:
            nombres_recetas=os.listdir(recetas_por_categoria)
            print("\nLas recetas actuales son:")
            for i,nombre in enumerate(nombres_recetas):
                receta=nombre
                print(i+1, receta)
            #eliminar receta
            eleccion_receta=int(input("Ingresa el número de la receta que quieres eliminar: "))
            receta_elegida=nombres_recetas[eleccion_receta-1]
            os.remove(Path(path_base,eleccion_categoria,receta_elegida))
            system("cls")
            print("La receta ha sido eliminada.")
            existe=False  
#!!!!!!!!!!!
#################### ELIMINAR CATEGORIAS ####################
def eliminar_categoria():
    path_base=os.path.abspath("Recetas")
    
    print("Estas son las categorías actuales:")
    nombre_de_categorias=os.listdir("Recetas")
    
    #mostrar categorias
    for i,nombre in enumerate(nombre_de_categorias):
        categoria=nombre
        print(i+1,') ',categoria)
    existe=True
    while existe==True:
        #eliminar categoria
        eleccion_categoria=int(input("Ingresa el número de la categoria que quieres eliminar: "))
        while eleccion_categoria>len(nombre_de_categorias) or eleccion_categoria<0:
            print("Has ingresado una categoria inválida.")
            eleccion_categoria=int(input("Ingresa el número de la categoria que quieres eliminar: "))
        categoria_elegida=nombre_de_categorias[eleccion_categoria-1]
        os.rmdir(Path(path_base,categoria_elegida))
        system("cls")
        print("La categoria ha sido eliminada.")
        existe=False     
#!!!!!!!!!!!
#################### CREAR CATEGORIAS ####################
def crear_categoria():
    path_base=os.path.abspath("Recetas")
    
    print("Estas son las categorías actuales:")
    nombre_de_categorias=os.listdir("Recetas")
    
    #mostrar categorias
    for nombre in nombre_de_categorias:
        categoria=nombre
        print("-",categoria)
    existe=True
    while existe==True:
        #crear categoria
        nombre_categoria_nueva=input("\nIngresa el nombre de la nueva categoría: ")
        nombre_categoria_nueva=nombre_categoria_nueva.capitalize()
        categoria_nueva=Path(path_base, nombre_categoria_nueva)
        categoria_nueva.mkdir()
        system("cls")
        print(f"La nueva categoria {nombre_categoria_nueva} ha sido creada.")
        break     
#!!!!!!!!!!!
#################### CREAR RECETAS ####################
def crear_receta():
    path_base=os.path.abspath("Recetas")
    
    print("Elije en qué categoría te gustaría agregar una receta.")
    nombre_de_categorias=os.listdir("Recetas")
    
    #mostrar categorias
    for nombre in nombre_de_categorias:
        categoria=nombre
        print("- ",categoria)
    #elegir categoria
    existe=True
    while existe==True:
        eleccion_categoria=input("Escribe el nombre de la categoría: ")
        eleccion_categoria=eleccion_categoria.lower().capitalize()
        recetas_por_categoria=Path(path_base,eleccion_categoria)
        if recetas_por_categoria.exists()==False:
            print("No existe esta categoría, ingresa nuevamente.")
            eleccion_categoria=input("Escribe el nombre de la categoría que te interesa:")
        else:
            nombres_recetas=os.listdir(recetas_por_categoria)
            print("\nLas recetas actuales son:")
            for nombre in nombres_recetas:
                receta=nombre
                print("- ", receta)
            #crear
            nombre_receta_nueva=input("\nIngresa el nombre de la receta: ")
            nombre_receta_nueva=nombre_receta_nueva.capitalize()+".txt"
            contenido_receta_nueva=input("Ingresa la receta: ")
            crear_receta=open(Path(path_base,eleccion_categoria,nombre_receta_nueva),'w')
            crear_receta.write(contenido_receta_nueva.capitalize())
            crear_receta.close()
            system("cls")
            print(f"La nueva receta {nombre_receta_nueva.capitalize()} ha sido creada.")
            break
#!!!!!!!!!!!

bienvenida()
#################### MENU OPCIONES ####################
repetir=True
while repetir==True:
    print("\nElije alguna de las siguientes opciones:")
    print('''    1. Leer una recetea de alguna categoría.
    2. Crear una receta. 
    3. Crear una categoría. 
    4. Eliminar una receta.
    5. Eliminar una categoría.
    6. Finalizar navegación por el recetario.''')
    eleccion=(input("> "))
    
    while eleccion.isdigit()==False:
        print("Has ingresado una opción incorrecta.")
        eleccion=(input("Ingresa nuevamente una opción del menú: "))
    if eleccion.isdigit()==True:
        eleccion=int(eleccion)
    while eleccion<1 or eleccion>6:
        print("Has ingresado una opción incorrecta.")
        eleccion=(input("Ingresa nuevamente una opción del menú: "))

    if eleccion==1:
        mostrar_recetas()
    if eleccion==2:
        crear_receta()
    if eleccion==3:
        crear_categoria()
    if eleccion==4:
        eliminar_receta()
    if eleccion==5:
        eliminar_categoria()
    if eleccion==6:
        system("cls")
        print("Programa finalizado.\n¡GRACIAS!\n")
        break









