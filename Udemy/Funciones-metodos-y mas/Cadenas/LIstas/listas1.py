#las listas en python son objetos mutables e iterables
from random import randint

# lista = ['nombre', 'nombre','nombre','nombre','nombre']

# for nombre in lista:
#     while True:
#         user = input("Que palabra deseas verificar si se encuentra: ")
#         if user in nombre:
#             print("Si esta",user)
#         else:
#             print(f"No esta la letra '{user}' ")


# Comprobar si el numero aletatorio generado es el indicado por el usuario

# cpu = randint(1,10)

# vidas = 5
# while True:
#     try:
#         intento = int(input("Ingresa un numero: "))
#         if intento > cpu:
#             print("El numero secreto es menor")
#             vidas - 1
#         elif intento < cpu:
#             print("El numero secreto es mayor")
#             vidas - 1
#         if intento == cpu or vidas < 0:
#             print(f"Felicidades, lo has logrado en {vidas} intentos")
#             break
#     except:
#         print("Debes de introducir un numero")


# Conversion de simbolos romanos a numeros decimales, es decir si se ingresa XX debera de regresar 20

def numero_romano(user_input):
    """Funcion para regresar un valor segun el introducido
       primero se haran pruebas hasta el 50
    """
    numeros = {
        'I':1,
        'II':2,
        'III':3,
        'VI':4,
        'V':5,
        'VI':6,
        'VII':7,
        'VIII':8,
        'IX':9,
        'X':10,
        'L':50,
        'C':100
    }
    suma = 0
    valores = []
    while suma < user_input:
        for clave,valor in numeros.items():
            resto = 0
            division = valor % user_input
            if division != 0:
                suma += resto
                valores.append(clave)
            division = resto
        if suma == user_input:
                print("se logro")
    return valores

print(numero_romano(17))

"""Si Alguno de los valores(keys) sumados(values) 
    es igual al introducido, se regresaran los que conformaron
    la suma
"""