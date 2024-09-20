# Metodo index()

# Un metodo que nos permite saber la ubicacion de un caracter

# mi_texto ="Esta noche salgo"
# #          ||||||||||||||||
# #          0123456789......
# resultado = mi_texto[0]

# resultado = mi_texto[-1]

# resultado = mi_texto.index("o")

# resultado = mi_texto.index("o",3,11)

# resultado = mi_texto.rindex("o")
#-----------------------------------------------------------------------------------------------------------------

#1) Práctica Método Index() 1
# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

# palabra = "ordenador"
# print(palabra[4])
#-----------------------------------------------------------------------------------------------------------------

#2) Práctica Método Index() 2
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."


# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
# print(frase.index("práctica"))
#-----------------------------------------------------------------------------------------------------------------

#3) Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

# print(frase.rindex("práctica",0,50))
#-----------------------------------------------------------------------------------------------------------------

# Metodo sub-strings

# texto="ABCDEF"
# fragmento = texto[2:10:2]
# print(fragmento)
# fragmento_inverso = texto[::-1]
# print(fragmento_inverso)

# Práctica Sub-Strings 1
# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:

#frase="Controlar la complejidad es la esencia de la programación"

# Pista: "Controlar" tiene un largo de 9 caracteres.

#print(frase[0:9])
#-----------------------------------------------------------------------------------------------------------------

# Práctica Sub-Strings 2
# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

# oracion="Nunca confíes en un ordenador que no puedas lanzar por una ventana"

# print(oracion[9::3])
#-----------------------------------------------------------------------------------------------------------------

# Práctica Sub-Strings 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

# frase="Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

# print(frase[::-1])
#----------------------------------------------------------------------------------------------------------------

# # Metodo strings 

# texto = "Este es un Texto"

# print(texto.upper()) #pone todo el texto en mayusculas 
# print(texto[2].upper())

# print(texto.lower())#ponete todo el texto en minusculas
# print(texto[2].lower())

# print(texto.split())# va a separar el texto en un lista 
# print(texto.split("e"))#separar el texto en un lista separando en ese caracter


# a="Aprender"
# b="Python"
# c="Es"
# d="Genial"
# e = " ".join([a,b,c,d]) #va a unir todos los elementos en una lista separando con un espacio 
# print(e)


# print(texto.find("un"))#encuatra como el index con la diferencia que no arroja ningun error 

# print(texto.replace("e","x")) #busca y reemplaza la primera letra con la segunda
#-----------------------------------------------------------------------------------------------------------------

# # Práctica Métodos de String 1
# oracion="Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:"
# print(oracion.upper())
#-----------------------------------------------------------------------------------------------------------------

# Práctica Métodos de String 2
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
# lista_palabras = ["La","legibilidad","cuenta."]
# union=" ".join(lista_palabras)
# print(union)
#-----------------------------------------------------------------------------------------------------------------

# Práctica Métodos de String 3
# Reemplaza en la siguiente frase:

#frase_1= "Si la implementación es difícil de explicar, puede que sea una mala idea."

# los siguientes pares de palabras:

# "difícil" --> "fácil"

# "mala" --> "buena"

# y muestra en pantalla la frase con ambas palabras modificadas.

# frase_2= frase_1.replace("difícil", "fácil")
# frase_3= frase_2.replace("mala","buena")

# print(frase_3)