Lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

# Definir una lista de números

# Inicializar la variable suma_pares
Suma_pares = 0
Suma_impares = 0
# Iterar sobre la lista y sumar solo los números pares a la variable suma_pares
for numero in Lista_numeros:
    if numero % 2 == 0:
        Suma_pares += numero # simbolo de reasignacion.

# Iterar sobre la lista y sumar solo los números pares a la variable suma_impares
for numero in Lista_numeros:
    if numero % 2 != 0:
        Suma_impares += numero

# imprimir los resultados
print("La suma de los numeros pares es", Suma_pares)
print("La suma de los numeros impares es", Suma_impares)
