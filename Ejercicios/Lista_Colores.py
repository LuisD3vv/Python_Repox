lista = []
print("Ingresa colores separados por comas.")
x = input(">> ")
lista.append(x)
# in situ
lista.sort()
# al reves
lista.sort(reverse=True)
# cra una nueva lista
nueva = sorted(lista)
print(lista)
print(nueva)