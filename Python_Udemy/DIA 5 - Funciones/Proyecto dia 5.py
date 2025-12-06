"""
Hecho por Luis Alejandro Aguilar Soberanes 28/01/2025 finalizado el 17/02/2025

Proyecto: Proyecto Final dia 5 Curso A_Udemy
    Descripcion: Juego del ahorcado basico

"""

import random

# LISTA DE PALABRAS

lista_palabras = ['luis','eduardo','gato','perro','git','elote','vape','capibara','coco','amargura']


# FUNCION QUE REGRESA UNA PALABRA AL AZAR
def random_word():
    palabra_aleatoria = random.choice(lista_palabras)
    return palabra_aleatoria


palabra = random_word()


# FUNCION SEPARA LA PALABRA EN LETRAS
def palabra_x_letra(palabrita):
    palabra_separada = list(palabrita)
    return palabra_separada


comparacion = palabra_x_letra(palabra)


guiones = ["_"] * len(comparacion)
vidas = 5
bucle = True

while bucle:
    print("============================")
    print("Adivina la siguiente palabra")
    print(" ".join(guiones))
    print("\n")

    intento = input("Ingresa una letra: ")
    acierto = False # se inicializa como false


    for i in range(len(comparacion)):
        if intento == comparacion[i]:
            guiones[i] = intento
            acierto = True # si hay al menos un acierto


    if not acierto:
        vidas -= 1
        print(f"Te quedan {vidas} intentos")

    if guiones == comparacion:
        bucle = False
        print("Felicidades, has adivinado!!, la palabra era: " + "".join(guiones).capitalize())
    elif vidas == 0:
        bucle = False