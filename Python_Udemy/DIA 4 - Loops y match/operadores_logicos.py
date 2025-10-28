# los operadores logicos se utuilizan para evaluar o modificar expresiones boolenas
# es decir, valores de verdadero o falso siendo 0 y 1 respectivamente


Verdad = True
Falso = False

"""
Las expresiones logicas son las siguientes

AND es true solo si ambas evaluciones son true
OR  es true si alguna de las evaluciones es true
NOT invierte el valor logico de la evaluacion

Ejemplo:

Esta_registrado = True

if not Esta_registrado: si no esta registrado
    print("Necesitas registrarte")
"""

mi_bool = (55 == 55) and ('perro' == "Perro")
texto = "esta frase es breve"
textito = ("frase" in texto) or ('breve' in texto)

lista = [1,2,3,4,5,6,7,8,9,10]

for n in lista:
    if n % 2 == 0:
        print(n)

print(mi_bool)
print(texto)
print(textito)
