mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(eliminado)

# ----------
# estos metodos no crean nuevas listas, solo modifican las instancias actuales
lista = ['g', 'o','b', 'm', 'c']
lista2 = [1, 3, 6,2,7,5,1]
lista.sort() # reorganizar elementos
#lista.reverse() # literalmente al reves
print(lista)
print(lista2)

# Para crear una nueva instancia se utiliza el metodo sorted
#para aplicar una funcion a un iterable o elementos se utiliza map o lamda, yield



# Ejemplo con lista de listas

print()
coches = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# los Indices comienzan desde el putisimo cero
print(coches[0][1])

# como en el pinche C a la verga
for i in range(len(coches)):
    for j in range(len(coches)):
        print(coches[i][j])