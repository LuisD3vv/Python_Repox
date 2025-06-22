from pathlib import Path,PureWindowsPath

# La ruta tiene que ser muy especifica
carpeta = Path('C:/Users/HP/Desktop/Python rutas/Prueba.txt') # Usar en linux

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)


print(carpeta.read_text())
"""
metodo de path para leer sin tanto rollo
Junto con otros metodos y funciones
"""

print(f"La ruta padre el archivo: '{carpeta.parent}'") # /home/lissandrito
print(f"Nombre del archivo: '{carpeta.name}'") # nombre del archivo .txt
print(f"La Extension del documento: '{carpeta.suffix}'") # tipo de archivo
print(f"El nombre sin extension: '{carpeta.stem}'") # documento o quitar extension

if carpeta.exists(): # verificar el archivo existe
    print("Este archivo Existe")
else:
    print("No existe")

# Lo opueto
if not carpeta.exists(): # verificar el archivo existe
    print("Este archivo no Existe")
else:
    print("Este archivo existe")