from pathlib import Path, pureWindowsPath

carpeta = Path('/home/lissandro/ejemplo udemy de rutas.txt')

#ruta_windows = pureWindowsPath(carpeta)
#print(ruta_windows)

if carpeta.exists():#verificar el archivo existe
    print("este archivo no existe")
else:
    print("Genial existe")

print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)