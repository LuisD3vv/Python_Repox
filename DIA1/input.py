import random
# a diferencia d eprint que solo imprime, input recibe los datos y puede guardar la variable
Nombre = input("Dime tu Nombre: ")
Apellido = input("Dime tu Apellido: ")

numero_identificacion = (random.randint(1, 9999))

print(f'{Nombre} {Apellido} tu ID es {numero_identificacion}')

print("Tu nombre es " + (input('Tu nombre: ')) + ' ' + (input('tu apellido: ')))
