#mi_archivo = open('Prueba.txt')

# print(mi_archivo.read())

# una_linea= mi_archivo.readline()
# print(una_linea)

# una_linea= mi_archivo.readline()
# print(una_linea.upper())

# una_linea= mi_archivo.readline()
# print(una_linea.splitlines())

# for l in mi_archivo:
#     print("Aqui dice: "+l)

# todas = mi_archivo.readlines()
# print(todas)
# todas = todas.pop()
# print(todas)

# mi_archivo.close()


#----------------------------------------------------------------------------------------------
# Práctica Abrir y Manipular Archivos 1
# Abre el archivo texto.txt e imprime su contenido.

# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código

# mi_archivo = open('Prueba.txt','a')
# mi_archivo.write("Hola! Wie geht´s")

# mi_archivo=open('Prueba.txt')
# print(mi_archivo.read())

# mi_archivo.close()

#----------------------------------------------------------------------------------------
# Práctica Abrir y Manipular Archivos 2
# Imprime la primera línea del archivo texto.txt
# No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código

# mi_archivo=open('Prueba.txt')
# primera_linea=mi_archivo.readline()
# print(primera_linea)

# mi_archivo.close


#----------------------------------------------------------------------------------------
# Práctica Abrir y Manipular Archivos 3
# Abre el archivo texto.txt e imprime únicamente la segunda línea.

# mi_archivo=open('Prueba.txt')
# primera_linea=mi_archivo.readline()
# primera_linea=mi_archivo.readline()
# primera_linea=mi_archivo.readline()
# primera_linea=mi_archivo.readline()
# print(primera_linea)

# mi_archivo.close

#----------------------------------------------------------------------------------------


# archivo = open('prueba.txt','r')
# archivo = open('prueba_nueva.txt','w')
# archivo = open('prueba.txt')
# archivo.write('hola\n')
# archivo.write('mundo')

# archivo.write('''hola 
#               mundo
#               soy 
#               programador de
#               python''')

# archivo.writelines(['hola','como','estas','?'])
# archivo.write('mundo')

# archivo = open('prueba.txt','a') 
# archivo.write("esta va a ser la ultima linea")
# archivo.close()

#----------------------------------------------------------------------------------------

# Práctica Crear y Escribir Archivos 1
# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

# Imprime el contenido completo de "mi_archivo.txt" al finalizar.

# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

# mi_archivo=open('Prueba.txt','a')
# mi_archivo.write("\n Nuevo Texto")
# mi_archivo.close
# mi_archivo=open('Prueba.txt','r')
# print(mi_archivo.read())
# mi_archivo.close

#----------------------------------------------------------------------------------------
# Práctica Crear y Escribir Archivos 2
# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga:
# "Nuevo inicio de sesión".

# Imprime el contenido completo de "mi_archivo.txt" al finalizar.

# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

# mi_archivo=open('Prueba.txt','w')
# mi_archivo.write("Nuevo inicio de sesión.")
# mi_archivo.close
# mi_archivo=open('Prueba.txt','r')
# print(mi_archivo.read())
# mi_archivo.close
#----------------------------------------------------------------------------------------

# Práctica Crear y Escribir Archivos 3
# Utiliza el método writelines para escribir los valores de la siguiente lista al final
# del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para
# separarlos.

# registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga\t"]

# el_archivo=open('registro.txt','a')
# el_archivo.writelines(registro_ultima_sesion)
# el_archivo.close

el_archivo=open('registro.txt','r')
print(el_archivo.read())
el_archivo.close

# Imprime el contenido completo de "registro.txt" al finalizar.

# Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t.
# También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.