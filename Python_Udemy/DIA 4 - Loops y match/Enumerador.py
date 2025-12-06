lista = ['a', 'b', 'c']

# enumerate es una función incorporada en Python
# se utiliza para agregar un contador a un iterable
# por cada iteracion, agregando asi un valor

mis_tuples = list(enumerate(lista))
print(mis_tuples)

# enumerador toma dos variables para ciclar
# es decir, una para el indice y otra pra el valor
# la podemos convertir en lista

lista = ["Luis","eduardo","aguilar"]

for indice, nombre in enumerate(lista):
    print(indice,nombre)
    
    
# es util para menus iteractivos

lista = ["Luis","eduardo","aguilar"]

for indice, nombre in enumerate(lista):
    print(indice,nombre)
    
print("Cual opcion quiere")
si = int(input("eleccion"))
match si: # type: ignore
    case 0:
        print("luis")
    case 1:
        print("eduardo")
    case 2:
        print("william")
    case _:
        print("culo")