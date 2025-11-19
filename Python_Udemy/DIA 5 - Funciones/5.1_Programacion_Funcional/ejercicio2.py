# Traductor
import os
from functools import reduce

# Funciones de orden mas alto (funciones anidadas)

'''
son las funciones que pueden tomar a una funcion como arugmento 
y regresar funciones como resultado
'''

os.system("clear")
def translator(lang):
    translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }
    def translator_word(word):
        if word.lower() in translations[lang]:
            return translations[lang][word.lower()]
        else:
            return 'Translarion not aviable'
    return translator_word


traduccion = translator('french')
print(traduccion('hello'))


# Example operation USING MAP
def double(x):
  return x * 2

# List of numbers
numbers_list = [1, 2, 3, 4, 5]

# Using the higher-order function
doubled_numbers = list(map(double, numbers_list))

# Displaying the outcomes
print('Original Numbers:', numbers_list)
print('Doubled Numbers:', doubled_numbers)

# Example operation USING FILTER, the input function in filter must return a boolean
# filter no hace desempaquetado de tuplas ya que los toma como al
def filter_even(x):
    return x % 2 == 0

even_numbers = filter(filter_even, [1, 2, 3, 4, 5])

print(list(even_numbers)) # Output: [2, 4]

# Reduce, toma un iterable y combina sus elementos para regresar un solo valor

# reduce(function,data,initial)

def tabla_multiplicar(x,y):
    return x * y

# la funcion solamente regresa un valor
prodcuto = reduce(tabla_multiplicar,[1,2,3,4,5]) #120
print(prodcuto)