# * que son los loop While

# El bucle while en Python es otra estructura de control que se utiliza para repetir un bloque de código mientras una condición dada sea verdadera. A diferencia del bucle for, que itera sobre una secuencia predefinida, el bucle while se ejecuta mientras una condición específica sea verdadera.

# La sintaxis general de un bucle while en Python es la siguiente:

# while condicion:
#     # Bloque de código a ejecutar mientras la condición sea verdadera

# Donde:

#  condicion es una expresión booleana que se evalúa en cada iteración del bucle. Mientras esta condición sea verdadera, el bloque de código dentro del bucle se ejecutará repetidamente.

#  Por ejemplo, si quieres imprimir los números del 0 al 5 utilizando un bucle while, puedes hacerlo de esta manera:

numero = 0

while numero <= 5:
    print(numero)
    numero += 1

# Este bucle while imprimirá los números del 1 al 5, ya que la condición numero <= 5 se evalúa como verdadera en cada iteración mientras numero sea menor o igual a 5.

# El bucle while es útil cuando no se conoce de antemano cuántas veces se debe ejecutar un bloque de código, ya que se ejecuta mientras la condición especificada sea verdadera. Sin embargo, es importante tener cuidado con las condiciones de salida del bucle para evitar bucles infinitos.
# -------------Ejercicio 1 ----------
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1  # en cada iteracion se le ira reduciendo uno
else:
    # hasta que se acaben las monedas y llegue al cero e imprmimira este mensaje
    print('no tengo mas dinero')

# -------------Ejercicio 2 ----------

respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir? (s/n): ')
else:
    print('Gracias')

# -------------Ejercicio 3 ----------

nombre = input('Tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)


lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4,
                 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]
for numeros in lista_numeros:
    if numeros < 0:
        break
    print(numeros)


 # el pass se utiliza como un ticket de entrada vacia en donde hace falta codigo pero aun no se implementa