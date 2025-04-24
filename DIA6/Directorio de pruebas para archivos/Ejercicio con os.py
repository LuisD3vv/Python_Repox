from pathlib import Path
import os

carpeta = Path('/home/lissandro/Escritorio/Ciencias de datos')
listar2 = Path("/home/lissandro/Escritorio")
listar = os.listdir("/home/lissandro/Escritorio")

print(listar2)

is_file = []
is_path = []

file = os.path.isfile("/home/lissandro/Escritorio/cuaderno_de_trabajo_de_computación_de_primer_grado(2).pdf")
archivo = os.path.isdir("/home/lissandro/Escritorio")

detalles = os.stat("/home/lissandro/Escritorio/practicas github/Hello git/hellogit.py")
print(detalles)

print(file)
print(archivo)


if carpeta.exists():
    print("La carpeta existe")
else:
    print("La carpeta no existe")
