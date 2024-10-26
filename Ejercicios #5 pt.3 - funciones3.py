#EJERCICIO 1
# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.

# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.

# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.

# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.

# def devolver_distintos(a,b,c):
#     suma_valores=a+b+c
#     if suma_valores>15:
#         lista_valores=[a,b,c]
#         mayor_a_menor=sorted(lista_valores)
#         print(f"El valor mayor entre los 3 numeros es {mayor_a_menor[2]}")
#     elif suma_valores<10:
#         lista_valores=[a,b,c]
#         mayor_a_menor=sorted(lista_valores)
#         print(f"El valor menor entre los 3 numeros es {mayor_a_menor[0]}")
#     elif suma_valores>=10 and suma_valores<=15:
#         print(f"El valor promedio entre los tres valores es {suma_valores/3}")


# x=float(input("Ingresa un primer numero: "))
# y=float(input("Ingresa un segundo numero: "))
# z=float(input("Ingresa un tercer numero: "))

# devolver_distintos(x,y,z)

#----------------------------------------------------------------------
# EJERCICIO 2
# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.

# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido", debería devolver ['d','e','i','n','o','r','t']

# def letras_ordenadas(letras):
#     letras_set=set(letras)
#     letras_lista=list(letras_set)
#     letras_lista.sort()
#     print(letras_lista)

# palabra=input("Ingresa una palabra: ")
# letras_ordenadas(palabra)

#----------------------------------------------------------------------
#EJERICIO 3
# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.

# Por ejemplo:

# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

# def ceros_consecutivos(lista):
#     lista_valores=list(lista)
#     control=False
#     cero=1
#     for i in lista_valores:
#         if i==cero and i==0:
#             control=True
#             break
#         else:
#             cero=i  
#     if control==True:
#         print(f"{lista_valores} >>> True")
#     else:
#         print(f"{lista_valores} >>> False")

# print("Ingrese los números que quiera. Para finalizar escriba FIN")
# valor=0
# lista_valores=[]

# while valor!="fin":
#     valor=input()
#     valor=valor.lower()
#     if valor != "fin":
#         valor=int(valor)
#         lista_valores.append(valor)

# ceros_consecutivos(lista_valores)

#----------------------------------------------------------------------
# EJERCICIO 4
# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.

# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.

# Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(a):
    a=int(a)
    valores=list(range(2,a+1))
    print(valores)
    lista_primos=[]
    for valor in valores:
        if valor%2!=0 and valor%3!=0 and valor%5!=0:
            lista_primos.append(valor)
        else:
            continue
    print(f"Los números primos entre 0 y {a} son: {lista_primos}")

limite=input("Ingrese un número mayor a 0: ")
contar_primos(limite)




