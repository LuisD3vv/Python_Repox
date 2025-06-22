import random
print("Bienvenido")
nombre, apellido = input("Ingresa tu nombre: ").split(" ")

print(f"muy bien, {nombre} {apellido} he pensado un numero entre 1 y el 100, tienes solo 8 intentos para adivinar, estas listo?"
      f"")

generador = random.randint(1, 101) # numero entre el 1 y el 100
intentos = 0
max_intentos = 8

while intentos < max_intentos:
    while True:
        numero = input("intenta adivinar el numero(1-100): ")
        try:
            numero = int(numero)
            if numero > 100 or numero < 0:
                print("ingresa un numero dentro del rango.")
            elif numero < generador:
                print("El numero es mayor")
                intentos += 1
            elif numero > generador:
                print("El numero es menor")
                intentos += 1

            if numero == generador:
                print(f"Felicidades {nombre} Has acertado el numero {generador} en el intento {intentos}")
                break

        except ValueError:
            print("ingresa un numero imbecil")

        if intentos == max_intentos:
            print("Te has quedado sin intentos")
            print(f"El numero era {generador}.")
            break
