# El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
# de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
# deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
# mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
# la palabra oculta, pierde una vida

#Datos:
# > 6 vidas
# > Descontar vidas cada vez que erra

from random import *

lista_palabras=["camello","leopardo","ornitorrinco", "ballena", "gaviota", "anaconda", "perro", "zorro", "tucan","orangutan","hipopotamo","ardilla","canguro", "lemur"]
vidas=6

print("Hola! Vamos a jugar! Te mostraré cuántas letras tiene una palabra sorpresa y tendrás 6 vidas. Cada intento fallido te restará 1 vida, si adivinas, podrás seguir jugando.\nUna pista! Es un animal!")

palabra_secreta=choice(lista_palabras)
print(f"La palabra secreta tiene {len(palabra_secreta)} letras.")
palabra_guiones=["_"]*len(palabra_secreta)
control=True

#
while control==True:
    print(" ".join(palabra_guiones))
    letra_usuario_primera=input("Ingresa una letra: ")
    letra_usuario=letra_usuario_primera.lower()
    if letra_usuario in palabra_secreta:
        for indice,letra in enumerate(palabra_secreta):
            if letra_usuario == letra:
                palabra_guiones[indice]=letra_usuario
    
    else:
        print(f'La letra "{letra_usuario.upper()}" no está en la palabra secreta')
        vidas=vidas-1
        if vidas>0:
            print(f"¡Cuidado! Te quedan {vidas} vidas.")
        

    if vidas==0:
        print("¡Te quedaste sin vidas! FIN DEL JUEGO")
        print(f"La palabra secreta era: {palabra_secreta.upper()}")
        control=False
    
    if "_" not in palabra_guiones:
        print(f"¡ADIVINASTE! Ganaste el juego.")
        print(f"La palabra secreta era: {palabra_secreta.upper()}")
        control=False

if palabra_secreta=="camello" and control==False:
    print("""                ,,__
        ..  ..   / o._)                   .---.
       /--'/--\  \-'||        .----.    .'     '.
      /        \_/ / |      .'      '..'         '-.
    .'\  \__\  __.'.'     .'          i-._
      )\ |  )\ |      _.'
     // \\ // \\
    ||_  \\|_  \\_
*** '--' '--'' '--'""")




       

