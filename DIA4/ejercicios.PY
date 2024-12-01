lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2,
                 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]  # Definir una lista de números

# Inicializar la variable suma_pares
suma_pares = 0
suma_impares = 0
# Iterar sobre la lista y sumar solo los números pares a la variable suma_pares
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero

# Iterar sobre la lista y sumar solo los números pares a la variable suma_impares
for numero in lista_numeros:
    if numero % 2 == 1:
        suma_impares += numero

# imprimir los resultados
print("La suma de los numeros pares es", suma_pares)
print("La suma de los numeros impares es", suma_impares)
