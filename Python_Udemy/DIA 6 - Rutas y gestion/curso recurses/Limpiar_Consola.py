from os import system

# Estrategia para limpiar la pantalla. es decir se limpia lo que se ingreso antes
# supongo que la libreria hace que se puedan utilizar parametros del pc, como gestion de rutas, documento y configuraciones incluso

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system("clear")

# los comandos varian el sistema operativo
print(f" Tu {nombre} y edad {edad}")
