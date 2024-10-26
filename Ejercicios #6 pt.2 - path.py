# from pathlib import * 

# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

# Recuerda importar Path del módulo pathlib, y utilizar el método home()

# ruta_base=Path.home()
# print("El path es: ", ruta_base)

#----------------------------------------------------------------------------------------------------------------
# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

# "Curso Python"
# "Día 6"
# "practicas_path.py"
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path

# ruta=Path(ruta_base, "Curso Python","Dia 6","practicas_path.py")
# print(ruta)

# print(ruta.exists())
#----------------------------------------------------------------------------------------------------------------
# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario

# ruta=Path(ruta_base, "Curso Python","Dia 6","practicas_path.py")
# print(ruta)

# print(ruta.exists())

#----------------------------------------------------------------------------------------------------------------

# from os import system

# nombre = input("Dime tu numbre : ")

# edad = input("Dime tu edad : ")

# system('cls')

# print(nombre)
# print(edad)

#----------------------------------------------------------------------------------------------------------------
# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).

# def abrir_leer(archivo):
#     abrir_archivo= open(archivo)
#     print(abrir_archivo.read())
#     abrir_archivo.close()

# print("Ingresa el nombre de un archivo: ")
# nombre_archivo=input()

# abrir_leer(nombre_archivo)

#----------------------------------------------------------------------------------------------------------------
# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

# def sobrescribir(archivo):
#     abrir_archivo=open(archivo,'w')
#     abrir_archivo.write("Contenido eliminado")
#     abrir_archivo.close

# nombre_archivo=input("Ingresa el nombre de un archivo:")
# sobrescribir(nombre_archivo)

#----------------------------------------------------------------------------------------------------------------
# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
# Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    abrir_archivo=open(archivo,'a')
    abrir_archivo.write("\nSe ha registrado un error de ejecución")
    abrir_archivo.close()
    abrir_archivo=open(archivo)
    print(abrir_archivo.read())
    abrir_archivo.close()

nombre_archivo=input("Ingrese el nombre de un archivo: ")
registro_error(nombre_archivo)