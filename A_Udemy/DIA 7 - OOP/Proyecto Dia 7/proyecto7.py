"""Modulo para importar numeros pseudoaleatorios"""
from random import randint
from datetime import datetime
# from pathlib import Path
from os import system
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # formato de impresion
class Persona:
    """
    Creacion de la base persona
    """
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    """Clase principal que hereda nombre y apellidos"""
    def __init__(self,nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        """Formatear la impresion"""
        return f"Nombre: {self.nombre} | numero de cuenta: \U0001F4B3 [-{self.numero_cuenta}-] | cantidad disponible:$ {self.balance}."
    def __len__(self):
        return f"El largo de tu cuenta es de {len(self.nombre)}"
    def retirar(self,retiro):
        """Realizar retiros guardamos y modificamos el atributo real segun el objeto"""
        menos = self.balance - retiro
        self.balance = menos
    def depositar(self,deposito):
        """Realizar depositos, guardamos y modificamos el atributo real segun el objeto"""
        mas = self.balance + deposito
        self.balance = mas
def crear_cliente():
    """
    Generar a los clientes, posteriormente se añadira la funcion
    para elegir entre crear o iniciar sesion
    """
    system("clear")
    print("Hola, Bienvenido, para comenzar,Ingresa los datos solicitados")
    nombre = input("Ingresa tu Nombre: ")
    apellido = input("Ingresa un Apellido: ")
    depo = input("\U000026A0 Necesitas un deposito minimo de $500 para aperturar tu cuenta, estas de acuerdo? (si-no): ")
    system("clear")
    balance = 0
    if depo == 'si':
        balance = 500
    elif depo == 'no':
        otra_cantidad = int(input("Ingresa otra cantidad: "))
        balance = otra_cantidad
    no_cuenta = randint(1, 1000) # 1000 pero no inclusivo, sera 999
    user = Cliente(nombre=nombre,apellido=apellido, balance=balance,numero_cuenta=no_cuenta)
    return user
def inicio():
    """
    El fin de esta funcion es el una ves creado el cliente, que mas tarde tambien
    se añadira la funcion de inicar sesion, este obtiene los datos recien ingresados
    y los transforma en un objeto(instancia) de la clase cliente, en la que puede 
    depositar, retirar o solamente conocer el estados de su cuenta
    """
    cliente_actual = crear_cliente() #Aqui creamos la instancia
    print(f"Hola {cliente_actual.nombre}, Bienvenido.")
    while cliente_actual.balance > 0:
        opcion = int(input("¿Que operación deseas realizar?\n1-Depositar\n2-Retirar\n3-Consultar saldo\n4-Salir\n"))
        if opcion == 1:
            system("clear")
            print("Has elegido depositar")
            balance_nuevo  = int(input("¿Cuanto vas a depositar: "))
            cliente_actual.depositar(balance_nuevo)
            print(f"Deposito de ${balance_nuevo} realizado con exito \U0001F389")
        elif opcion == 2:
            system("clear")
            print("Has elegido Retirar")
            try:
                #Decirle al programa como manejar los errores
                balance_nuevo  = int(input("¿Cuánto vas a retirar: "))
                if balance_nuevo > cliente_actual.balance:
                    raise ValueError("Fondos insuficientes \U0000274C")  # Lanza un error manualmente/se usar cuando un valor no es valido para una operacion
                cliente_actual.retirar(balance_nuevo)
                print(f"Retiro de ${balance_nuevo} realizado con exito \U0001F389")
            except ValueError as error:
                print(f"Error: {error}")
                print(f"Puedes retirar un máximo de ${cliente_actual.balance}")
        elif opcion == 3:
            system("clear")
            print("Datos de la cuenta:")
            print(cliente_actual)
            # print(type(cliente_actual))
            # print(Cliente.__mro__)
        elif opcion == 4:
            system("clear")
            print(f"Hasta pronto {cliente_actual.nombre} \U0001F44B\nUtimo acceso -{fecha}")
            break
    if cliente_actual.balance <= 0:
        print(f"Has Agotado tus ahorros, ingresa de nuevo o realiaza un deposito\nUtimo acceso {fecha}")
#Iniciar loop y llamar a la funcion inicio

inicio()
#End of file
