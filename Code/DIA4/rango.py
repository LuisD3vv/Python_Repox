# for numero in range(9, 31, 2):
#     print(numero)


# lista = list(range(1, 101))

# print(lista)


valores = range(1, 16)

for numeros in valores:
    suma_cuadrados = sum(numeros ** 2 for numeros in valores)

    print(suma_cuadrados)
