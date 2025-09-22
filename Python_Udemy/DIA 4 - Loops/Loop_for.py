"""
Que son los loop for
Un bucle for en Python es una estructura de control 
que se utiliza para iterar sobre una secuencia 
(como una lista, una tupla, un diccionario, una cadena de caracteres, etc.)
y ejecutar un bloque de código una vez para cada elemento de esa secuencia.
La sintaxis general de un bucle for en Python es la siguiente:

for elemento in secuencia:
Bloque de código a ejecutar para cada elemento

Donde:

elemento es una variable que toma el valor
de cada elemento en la secuencia en cada iteración del bucle.
secuencia es la secuencia sobre la que se está iterando
como una lista, tupla, rango, cadena de caracteres, etc.
"""
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
"""
Este bucle for imprimirá cada número en la lista numeros en una línea separada.

El bucle for en Python es muy versátil y puede utilizarse para iterar sobre una variedad de objetos y tipos de datos, lo que lo convierte en una herramienta muy útil en la programación.

"""

# ----------- EJERCICIO 1 --------------------------

lista = ['A', 'B', 'C','D']

for letra in lista:  # el elemento despues del for puede ser cualquiera, pero se recomienda que sea algo relacionado con la lista
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

# ----------- EJERCICIO 2 --------------------------

lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'):  # startwith, significa que inicia con
        print(nombre)

# ----------- EJERCICIO 3 --------------------------

numeros = [1, 2, 3, 4, 5]
mi_valor = 0


for numero in numeros:
    mi_valor += numero
    print(mi_valor)

# ----------- EJERCICIO 4 --------------------------

palabra = 'python es genial'


for letra in palabra:
    print(letra)

# ----------- EJERCICIO 5 --------------------------

for a, b in [[1, 2,], [3, 4], [5, 6]]:  # asi se itera una lista dentro de otra lista
    print(a)
    print(b)

# ----------- EJERCICIO 6 --------------------------

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for a, b in dic.items():
    print(a, b)

# ----------- EJERCICIO 7 --------------------------
"""
Cuando queremos verificar una condicion y esta depende de la indentacion actual del codigo.
"""

for num in range(3):
    print(f"El numero actual es: {num}")
print("Bucle terminado")

