# 1 Declara dos variables, llamadas nombre y edad.
#   Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.

#Nombre=str
#Edad=int
#Nombre= "Tony Soprano"
#Edad= "51"
#print(Edad, Nombre)
#--------------------------------------------------------------------------------
# 2 Crea tres variables:
    #nombre
    #apellido
    #nombrecompleto
# A nombre, asígnale el valor "Julia", y en apellido,
#asigna el valor "Roberts". Finalmente,
#construye la variable nombrecompleto concatenando
#las variables (recuerda sumar un espacio intermedio).

#Nombre= "Julia"
#Apellido= "Roberts"
#nombreCompleto= Nombre + " " + Apellido
#print(nombreCompleto)

#--------------------------------------------------------------------------------
# 3) Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la fr
#Estás tomando un curso de curso
#Para ello deberás concatenar la primera parte de la
# frase con el valor que asumirá la variable.
# Recuerda agregar un espacio antes de concatenar la
# variable al resto del texto.

# curso=str
# curso='Python'

# print('"Estás tomando un curso de curso ' + curso + '"')
#--------------------------------------------------------------------------------

# 4)Práctica con Integers
# Declara una variable numérica llamada num_entero que contenga un valor de tipo intege
# de tu elección.

# num_entero=int
# print ("Ingrese un numero: " + input(num_entero))
#--------------------------------------------------------------------------------

# 5)Práctica con Floats
# Declara una variable numérica llamada num_decimal que contenga un valor de tipo float

# Imprime el tipo de dato de dicha variable.

# num_decimal = 25.8
# print(num_decimal, "es", type(num_decimal))
#--------------------------------------------------------------------------------

# 6)Práctica con Tipos de Datos Numéricos
# ¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificar
# Para ello, crea dos variables:

# num1 = 7.5

# num2 = 2.5

# A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos n

# num1 = 7.5
# num1 = float(num1)    
# num2 = 2.5
# num2 = float(num2)
# num3 = num1 + num2
# num3 = float(num3)

# print (num3, type(num3))
#--------------------------------------------------------------------------------

# 7) Práctica con Conversiones 1
# Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:

# num1 = 7.5
# num1 = int(num1)

# print (num1, type(num1))
#--------------------------------------------------------------------------------

# 8)Práctica con Conversiones 2
# Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:

# num2 = 10
# num2 = float(num2)

# print (num2, type(num2))
#--------------------------------------------------------------------------------

## 9) Práctica con Conversiones 3
# Suma los valores de num1 y num2.
# No modifiques el valor de las variables ya declaradas,
# sino aplica las conversiones necesarias dentro de la función print().

# num1 = "7.5"
# num2 = "10"

# print(float(num1) + float(num2))
#--------------------------------------------------------------------------------

# 10) Práctica Formatear Cadenas 1
# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación),
# es muy importante para llegar al resultado correcto.

# nombre_asociado = "Jesse Pinkman"
# numero_asociado = 399058

# print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")
#--------------------------------------------------------------------------------

# 11) Práctica Formatear Cadenas 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación),
# es muy importante para llegar al resultado correcto

puntos_nuevos = 350
puntos_totales = 1225

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
