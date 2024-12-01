import random
print("Bienvenido")
nombre = input("Cual es tu nombre: ")

print(f"muy bien {nombre} he pensado un numero entre 1 y el 100, tienes solo 8 intentos para adivinar")

# generador = random.randint(1, 101)
generador = 89
intentos = 0
max_intentos = 8

while intentos < max_intentos:
    numero = int(input("intenta adivinar el numero(1-100): "))

    if numero == generador:
        print(f"Felicidades {nombre} Has acertado el numero en el intento {intentos}")
        break
    elif numero > 100 or numero < 0:
        print("ingresa le numero correcto")
    elif numero < generador:
        print("Has elegido un numero menor")
        intentos += 1
    elif numero > generador:
        print("Has elegido un numero mayor")
        intentos += 1
if intentos == max_intentos:
    print("Te has quedado sin intentos")
