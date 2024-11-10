from os import system

class Persona():
    def __init__(self,nombre,apellido) -> None:
        self.nombre=nombre
        self.apellido=apellido
        pass

class Cliente(Persona):
    def __init__(self,nombre,apellido, numero_cuenta, saldo) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo             
    def imprimir_cliente(self):
        system('cls')
        print(f"Señor(a) {self.nombre} {self.apellido}:\nUsted posee en su cuenta número {self.numero_cuenta}, un saldo acumulado de ${self.saldo}.")
    def depositar(self):
        deposito=float(input("Ingrese el monto a depositar: $"))
        self.saldo=self.saldo+deposito
        system('cls')
        print(f"Su saldo actual es ${self.saldo}")
        return self.saldo
    def retirar(self):
        retiro=float(input("Ingrese el monto que desea retirar: $"))
        while self.saldo<retiro:
             system('cls')
             print(f"Saldo actual: ${self.saldo}")
             print("Su saldo es insuficiente para realizar esta extracción.")
             retiro=float(input("Ingrese el monto que desea retirar: $"))
        self.saldo=self.saldo-retiro
        system('cls')
        print(f"Su saldo actual es ${self.saldo}")
        return self.saldo


################## CREAR UNA PERSONA ##################
def nombre():
        nombre=input("Ingrese su(s) nombre(s): ")
        nombre=nombre.title()
        return nombre
def apellido():
        apellido=input("Ingrese su(s) apellido(s): ")
        apellido=apellido.title()
        return apellido

################## CREAR UNA CUENTA ##################
def crear_cuenta(): 
        print('Ingrese su número de documento (sin puntos ni espacios):')
        numero_cuenta=int(input())
        return numero_cuenta

################## CREAR UN CLIENTE (persona+cuenta) ##################
print("Bienvenido al sistema de gestión de cuentas bancarias.\n")
nombre_cliente=nombre()
apellido_cliente=apellido()
cuenta_nueva=crear_cuenta()

ejecutar=True
while ejecutar:
    print(f'''\nSr(a) {nombre_cliente} {apellido_cliente}, elija una de las siguientes opciones:
        1) Para crear una cuenta a su nombre.
        2) Para realizar un depósito.
        3) Para realizar una extracción.
        0) Para salir.''')
    opcion_elegida=int(input("> "))

    if opcion_elegida==1:
            print(f'Su numero de cuenta será: {cuenta_nueva}')
            print("Ingrese el saldo inicial de su cuenta: ")
            saldo=float(input("$ "))
            cliente_nuevo=Cliente(nombre_cliente,apellido_cliente,cuenta_nueva, saldo)
            cliente_nuevo.imprimir_cliente()
    
    if opcion_elegida==2:
         cliente_nuevo.depositar()

    if opcion_elegida==3:
         cliente_nuevo.retirar()

    if opcion_elegida==0:
        system('cls')
        print("Sistema de gestión bancaria FINALIZADO.\n ¡Gracias!\n")
        ejecutar=False




    



