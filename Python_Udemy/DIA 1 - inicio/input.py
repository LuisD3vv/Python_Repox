import random
"""Importar modulo random"""

# a diferencia de print que solo imprime, input recibe los datos y puede guardar la variable
Nombre = input("Dime tu Nombre: ")
# Input tambien puede ser una variable vacia tal como aqui

print("Abajo escribe el mensaje (cuando termines, escribe 'FIN') ")
Contenido = []
lista = []
while True:
    linea = input()
    if linea.upper() == "FIN":
        break
    lista.append(linea)
    Contenido = "\n".join(lista)

print(repr(Contenido))

Apellido = input("Dime tu Apellido: ")

numero_identificacion = random.randint(1, 9999)

print(f'{Nombre} {Apellido} tu ID es {numero_identificacion}')

print("Tu nombre es " + (input('Tu nombre: ')) + ' ' + (input('tu apellido: ')))
