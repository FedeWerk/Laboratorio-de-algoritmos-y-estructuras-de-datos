# La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
# ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
# poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
# letras a su elección y a partir de ese momento nuestro código va a procesar esa información
# para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
# 1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
# recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
# que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
# debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
# y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
# encuentren absolutamente todas las letras es pasar, tanto el texto original como las
# letras a buscar, a minúsculas.
# 2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
# para lograr esta parte, recuerda que hay un método de string que permite transformarlo
# en una lista y que luego hay una función que permite averiguar el largo de una lista.
# 3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
# claramente echaremos mano de la indexación.
# 4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
# las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
# que permita unir esos elementos con espacios intermedios? Piénsalo.
# 5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
# texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
# puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
# manera de expresarle al usuario tu respuesta.

print("Buenas! Te invito a que analicemos un texto juntos.")
texto= input("Ingresa el texto que analizaremos: ")

print("Ahora te invio a que ingreses 3 letras, así veremos algunas curiosidades del texto")
x=input("Primera letra:")
y=input("Segunda letra:")
z=input("Tercera letra:")
lista_letras= [x, y, z]
#Te vas Alfonsina vestida de mar
texto_minus=texto.lower()

# Punto 1. Indicar cuantas veces se repite cada letra seleccionada.
print(" ")
print(f"En el texto, la letra '{x.upper()}' aparece {texto_minus.count(x.lower())} veces")
print(f"En el texto, la letra '{y.upper()}' aparece {texto_minus.count(y.lower())} veces")
print(f"En el texto, la letra '{z.upper()}' aparece {texto_minus.count(z.lower())} veces")

# Punto 2. Informa cuantas palabras tiene el texto.
lista_texto=texto_minus.split()
print(f">>> INTERESANTE! Tu texto cuenta con {len(lista_texto)} palabras")

# Punto 3. Informa la 1ra letra del texto y la ultima-
print(f">>> La primera letra de tu texto es '{texto[0]}' y la última letra es '{texto[-1]}'")

#print(texto_minus)

# Punto 4. Mostrar el texto con el orden las palabrasinvertidas.
texto_reves=texto.split()
print(texto_reves[::-1])     #opcion 1. creasr la lista y recorrerla en reversa con paso -1 [(inicio):(fin):-1]

texto_reves.reverse()        #opcion 2. utilizar la funcion ".reverse()" que ordena al reves los elementos de una lista
print(texto_reves)

# Punto 5. Informar si aparece la palabra "Python" en el texto.

for palabra in lista_texto:
    if palabra == "python":
        print("¡Y qué loco! En el texto aparace la palabra 'Python'")
        break
    else:
        continue
    print("Pude notar, que en tu texto no aparece la palabra 'Phython'")


