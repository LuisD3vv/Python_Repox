
from random import choice
from functools import reduce
'''

Una función lambda en Python es una función anónima pequeña 
y de una sola línea que puede tener múltiples argumentos 
pero solo una expresión.
Se definen con la palabra clave lambda y son útiles para operaciones simples y rápidas, 
a menudo pasadas como argumentos a funciones de orden superior como map, filter y sorted
'''
numeros = list(range(1,11))
suma = list(map(lambda a: a**2,numeros))
print(suma)

# sinxtis corta de lambda
suma = lambda x,y: x + y
suma(3,5) # asi le pasamos los argumentos



'''
Funciones puras de aqui en adelante
'''

def fire_in_name(name):
    return True if "fire" in name.lower() else False

def concatenate_names(name1,name2):
    return name1 + ', ' +  name2
    
prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

# Generar nombres mayusculas

sufijos_mayusculas = list(map(capitalize_suffix,suffixes))

# Crear 10 nombres de fantasias

def create_fantasy_name(list_1, list_2):
    return choice(list_1) + ' ' + choice(list_2)

# generar los diez nombres aleatorios

random_names = [create_fantasy_name(prefixes,sufijos_mayusculas) for i in range(10)]

fireInName = list(filter(fire_in_name,random_names))

concatenar_nombres = reduce(concatenate_names, fireInName, '')

# 
def display_name_info():
    '''
    Prints the generated fantasy names with a for loop.
    Prints the filtered names that include 'Fire'.
    Prints the reduced name
    '''
    print("1")
    for fanName in random_names:
        print(fanName)
    print("2")
    print(f"Nombres con 'Fire': {fireInName}")
    print("3")
    print(f"Nombres concatenados {concatenar_nombres}")
display_name_info()