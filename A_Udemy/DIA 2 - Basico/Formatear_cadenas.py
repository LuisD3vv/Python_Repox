# Hay dos formas de lograr esto:

# * 1.- Funcion format

color = 'rojo'
matricula = 200489

print('mi auto es de color {} con matricula {}'.format(color, matricula))

# * 2. - Cadenas Literales

print(f'mi auto es de color {color} con matricula {matricula}')


# * una suma utilizando el formateo de cadenas seria algo asi

# * Declarando las variables

A = 10
B = 5
# Funcion format
print("La suma de {} y {} es igual a {}".format(A, B, A+B))
# cadenas literales
print(f'La suma de {A} + {B} da como resultado {A + B}')


puntos_nuevos = 350
puntos_totales = 1225

print(" Has ganado {} puntos! En total, acumulas {} puntos".format(
    puntos_nuevos, puntos_totales))
