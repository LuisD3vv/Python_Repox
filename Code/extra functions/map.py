#map funciona como una funcion que le aplica una funcion a un iterable
def cuadrado(n):
    return n * n


lista = [1,2,3,4,5,6,7,89]

print(list(map(cuadrado, lista)))