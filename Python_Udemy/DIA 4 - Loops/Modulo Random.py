from random import choices,randint,uniform,Random,shuffle,choice # type: ignore

colores = ['azul', 'rojo', 'verde', 'amarillo']

# selecciona una cantidad k de elementos aleatorios de un iterable
aleatorio:str = choices(colores,k=2) # type: ignore
print(aleatorio)
#selecciona un elemento aleatorio
aleatorio2:str = choice(colores)
# mezcla
numero = list(range(5, 50, 5))
shuffle(numero)

# genera numero aleatorios en un rango
aleatorio:int = randint(1,99)

# imprime valores del cero al uno
lista:str = ["Luis","eduardo","William"] # type: ignore

print(uniform(lista, b=2)) # type: ignore
