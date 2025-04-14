import os
# La libreria
from pathlib import Path

# ruta = os.path.isfile()
# ruta = os.path.isdir()
# ruta = os.path.exist()
# ruta = os.listdir()
# ruta = os.makedirs()
# ruta = os.rename()
# ruta = os.getcwd()
# ruta = os.chdir("/home/lissandro/Descargas/hombres.csv") cambiar de directorio
# ruta = os.makedirs() crear directorio util para el proyecto 6
# ruta = os.path.split()
# os.rmdir('ruta') eliminar directorio util para el proyecto 6
#os.stat()
# otro_archivo = open('prueba.txt')

carpeta = Path('/home/lissandro/') / 'ejemplo udemy de rutas'  # ruta de path

mi_archivo = open(carpeta)
print((mi_archivo.read()))