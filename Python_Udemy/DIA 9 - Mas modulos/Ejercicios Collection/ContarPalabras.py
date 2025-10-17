from collections import defaultdict
from pathlib import Path
from colorama import Fore, Back,Cursor

ruta = Path("texto.txt")
apariciones = defaultdict(int)
textoLimpio = []

print("Bienvenido, Escribe lo que deseas aqui abajo (FIN para salir):")
with open (ruta,"w") as lec:
    lineas = []
    while True:
        texto = input("> ")
        if texto.upper() == "FIN":
            break
        lineas.append(texto.lower())
    contenido = " ".join(lineas)
    lec.writelines(contenido)

print("Lo que escribiste fue")
with open (ruta,"r") as leer:
    lineas = leer.readlines(10)
    for linea in lineas:
        if linea in ('.',',','@','_',';',':','\n'):
            continue
        print(linea)
        textoLimpio.append(linea.strip().split())
        
for palabra in textoLimpio:
    for subpalabra in palabra:
        apariciones[subpalabra] += 1

print("Aparicion de cada palabra en el texto")
print(apariciones)

"""

:Detalles
replace
count
strip
find

"""