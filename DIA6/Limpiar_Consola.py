from os import system

# Estrategia para limpiar la pantalla. es decir se limpia lo que se ingreso antes
# supongo que la libreria hace que se puedan utilizar parametros del pc

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system("cl")

print(f" Tu {nombre} y edad {edad}")