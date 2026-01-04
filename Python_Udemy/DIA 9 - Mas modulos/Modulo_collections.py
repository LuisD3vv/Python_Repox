from collections import Counter, defaultdict, namedtuple, deque


#  Modulos mas importantes de collection


# Counter sirve para contar la cantidad de vecesq ue aparece un elemento, ya sea numerico o string
numeros = [83, 4, 5, 6, 7, 6, 56, 5, 4, 4, 3]
nombres = 'al pan pan y al vino vino'

serie = Counter([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 12])
print(serie.most_common()) # sin parametros
print(serie.most_common(5)) # con parametros
print(list(serie)) # Al imprimirlo en forma de lista se eliminan duplicados


# defaultdict

mi_diccionario = defaultdict(lambda: 'nada') # crea valores y claves por defecto para los diccionarios
mi_diccionario['1'] = 'rojo'
print(mi_diccionario['2'])


mi_dict = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dict['dos'])

# Otro ejemplo

mi_diccionario2 = defaultdict(lambda:'Valor no hallado')

mi_diccionario2['edad'] = 44

#  namedtuple, creamos un objeto con sus cracteristicas
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
luis = Persona('Lissandro', 1.96, 96)

# Creando una tupla con un solo elemento (se le coloca coma)
mi_tupla = (500,)

# por dot point

print(luis.nombre)
print(luis.altura)
print(luis.peso)

# impresion por indice

print(luis[0])
print(luis[1])
print(luis[2])

"""
Una cola doblemente terminada o deque, es una estructura de datos lineal que permite
Insertar y eliminar elementos por ambos extremos

"""

# Definimos el maximo largo, una ves alcanazo este, se eliminara el primer elemento si agregamos mas
# sintaxis es nombre = deque([])
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# Agregar elemento al final
lista_ciudades.append('Culiacan')
# Agregar elementos al inicio
lista_ciudades.appendleft('Washingthon')
print(lista_ciudades)
# sacar del final
lista_ciudades.pop()
# sacar elementos del incio
lista_ciudades.popleft()
print(lista_ciudades)
lista_ciudades2 = deque(["Stalingrado", "Jalisco", "Salt Lake City"])
# Agrega los elementos de otro iterable al final
lista_ciudades.extend(lista_ciudades2)
# Agrega los elementos de otro iterable al inicio
lista_ciudades.extendleft(lista_ciudades2)
print(lista_ciudades)
# agregar elementos en una posicion especifcia
print(lista_ciudades.insert(2, "Mechico"))