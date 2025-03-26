from pathlib import Path
#pureWindowsPath

carpeta = Path('/home/lissandro/ejemplo udemy de rutas.txt')

# ruta_windows = pureWindowsPath(carpeta)
# print(ruta_windows)

if carpeta.exists():# verificar el archivo existe
    print("este archivo no existe")
else:
    print("Genial existe")

print(carpeta.parent) # /home/lissandrito
print(carpeta.name) # nombre del archivo .txt
print(carpeta.suffix) # tipo de archivo
print(carpeta.stem) # documento