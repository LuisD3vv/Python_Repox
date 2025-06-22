import os
from pathlib import Path

#
# nombre = input("Ingresa tu nombre: ")
#
# with open("saludo.txt", "w") as archivo:
#     archivo.write(f"Hola {nombre}. Bienvenido al curso.")
#
# with open("saludo.txt") as lectura:
#     print(lectura.read())
#
# lista_de_tareas = ["Estudiar Python\n", "Leer 10 páginas\n", "Hacer ejercicio\n"]
# with open("tareas.txt", "w") as archivo2:
#     archivo2.writelines(lista_de_tareas)
# # Writelines no agrega saltos linea automaticamente.
#
# with open("tareas.txt") as lectura2:
#     print(lectura2.read())

# mas sencillo
ruta = os.listdir("documentos")
for archivo in ruta:
    if archivo.endswith(".html"):
        print(archivo)

usuario = input("Ingresa el nombre del archivo: ")

sinex = usuario.removesuffix(".html") + ".html"

ruta_archivo = Path("documentos") / sinex
print(ruta_archivo)
if os.path.exists(ruta_archivo):
    os.remove(ruta_archivo)
    print("Archivo borrado")
else:
    print("Archivo no encontrado")
