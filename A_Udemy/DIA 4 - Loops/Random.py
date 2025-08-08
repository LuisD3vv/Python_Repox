from random import *


colores = ['azul', 'rojo', 'verde', 'amarillo']

aleatorio = choice(colores)
print(aleatorio, k=1)


numero = list(range(5, 50, 5))

shuffle(numero)

print(numero)
