# Ejemplo sencillo de lectura
# existen 3 diferentes tipos de archivo r,a y w
"""
r sirve para leer el archivo e imprmir sus lineas
a sirve para escribir al ultimo del elemento, util para hacer logs
w sirve para modificcar o crear un archivo.
"""
lectura = open("prueba.txt", 'r')

print(lectura.read())


lectura.close() # buena practica cerrar el loop.