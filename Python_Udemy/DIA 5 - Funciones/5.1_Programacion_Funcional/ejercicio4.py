'''
Compresion de listas

list comprehesion can trasnform data, filter elements and even create nested list
no cambia la lista original, si no que crea otra.
solo funciona con loop for internamente
'''

# Sintax

# [expression for item in dataset if condicion]

# si no lleva expresion, esta se cambia asi (si solo se quiere filtrar)

# [item for item in dataset if condicion]

'''
expresion es lo que aplicara a cada elemento del iterable
item es cada elemento del iterable
dataset es el iterable lista, diccionario etc
condicion es opcional pero filtra los elementos
'''

# Ejercicio de codedex


numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
resultado = [n for n in numbers if n %2== 0] # filtrado
double = [n**2 for n in numbers if n %2== 0] # con operacion
print("Original {}".format(numbers))
print("Pares {}".format(resultado))