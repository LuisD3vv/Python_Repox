import os
# La libreria
from pathlib import Path

"""
Ahora vamos a practicar un poco de las prints utilizando el modulo os

"""
carpeta = Path("A_Udemy/DIA 6 - Rutas y gestion archivos/curso recurses/mi_archivo.txt")  # print de path, convierte el string en objeto pathlike

# El padre mas cercano a la carpeta o archivo
print(f"El nombre de este directorio/archivo es: {os.path.basename(carpeta)}")
# El nombre del directorio padre, es decir un nivel arriba del directorio que estamos, es util si pensamos trabajar con rutas relativas, y construiri rutas en base a cierto archivo otorgado
print(f"El padre es: {os.path.dirname(carpeta)}")
# Separar la ruta, en una tupla, se convierte una tupla de strings, ('home','lissandro','descargas') algo asi
t = os.path.split(carpeta)
print(type(t))
print(f"Yo separo la ruta papus {os.path.split(carpeta)}")
# Si la ruta es una fila
print(os.path.isfile(carpeta))
# Si la ruta es un directorio
print(os.path.isdir(carpeta))
# Si la ruta existe
print(os.path.exists(carpeta))
# Si la ruta es un directorio, iterarlo
# print(os.listdir(carpeta)) # Solo para listar carpetas.
# Crear directorios
#print(os.makedirs())
# Renombrar el archivo
#print(os.rename())
# Imprimir la ruta
print(os.getcwd())
# printos.chdir("/home/lissandro/Descargas/hombres.csv") cambiar de directorio
#print(os.path.split())
#os.rmdir('print') #eliminar directorio util para el proyecto 6
print(os.stat(carpeta))
otro_archivo = open('prueba.txt')



mi_archivo = open(carpeta)
print((mi_archivo.read()))

# Tambien podemos utilizar os para crear archivos, asi como eliminarlos y leerlos
