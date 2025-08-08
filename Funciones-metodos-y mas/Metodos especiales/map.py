#  map funciona como una funcion que le aplica una funcion a un iterable
def cuadrado(n):
	return n * n


lista = [1, 2, 3, 4, 5, 6, 7, 89]

#print(list(map(cuadrado, lista)))


#  La funcion map aplica una funcion a cada elemento de un iterable
#  La funcion filter aplica una filtro a cada elemento de un iterable

# Ambos necesitan ser convertidos a lista antes de poder operar con ellos

palabras = ['a', 'e', 'i', 'o', 'u']
print(list(map(lambda p: p.upper(), palabras)))

# Otro ejemplo

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sin convertirlo a list, filter regresa un objeto filter
# filter(funcion,iterable) Funcion filtro
filtrados = list(filter(lambda num: num % 2 == 0, numeros))

# sin convertirlo a list, filter regresa un objeto map
# map(funcion,iterable) Cualquier funcion
multiplicados = list(map(lambda x: x * 2, filtrados))

print(f"Numeros originales => {numeros}")
print(f"Numeros filtrados => {filtrados}")
print(f"Numeros filtrados multiplicados => {multiplicados}")
"""
Devuelve un objeto map
que puedes convertir en list()
"""
