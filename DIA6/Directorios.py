import os
# La libreria
from pathlib import Path


#ruta = os.getcwd()
#ruta = os.chdir("/home/lissandro/Descargas/hombres.csv")
#ruta = os.makedirs()
#ruta = os.path.split()
#os.rmdir('ruta') eliminar
#otro_archivo = open('prueba.txt')

carpeta = Path('/home/lissandro/')  / 'ejemplo udemy de rutas'  # ruta de path

mi_archivo = open(carpeta)
print((mi_archivo.read()))