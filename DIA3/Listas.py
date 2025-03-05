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
lista.reverse() # literalmente al reves
print(lista)
print(lista2)