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
os.system("clear")
ruta_documentos = os.path.join(os.path.dirname(__file__),"documentos/")
ruta = os.listdir(ruta_documentos)
print("Archivos extension [.html] disponibles:")
for archivo in ruta:
    if archivo.endswith(".html"):
        print(archivo)

#listdir, devuelve una lista con los elementos que se encutran
# es decir que si quisieramos saber si esta vacia deberiamos compararla con
#una lista vacia.

# tambien se puede con if not os.listdir(ruta)
if not os.listdir(ruta_documentos):
    print("No hay documentos disponibles.")
    crear = input("Quieres crear uno?: ")
    if crear == "si":
        arch = input("ingresa el nombre del archivo: ")
        ruta_nueva = Path(ruta_documentos + arch + ".html")
        ruta_nueva.touch(exist_ok=True)
        print(f"Archivo creado en {ruta_nueva}")
        # ruta_documentos.joinpath(arch + ".html")
else:
    while True:
        try:
            print("Que quieres hacer:\n1-Eliminar\n2-Agregar")
            opcion = int(input("Opcion: "))
            match opcion:
                case 1:
                    print("Ingresa el nombre del archivo, para salir escribe (salir)")
                    usuario = input("Nombre del archivo: ").lower()
                    sinex = usuario.removesuffix(".html") + ".html"
                    if "salir" == usuario.lower():
                        break
                    else:
                        ruta_archivo = Path("documentos") / sinex
                        print(ruta_archivo)
                        if os.path.exists(ruta_archivo):
                            os.remove(ruta_archivo)
                            print(f"Archivo {sinex} borrado")
                            break
                        else:
                            print("Archivo no encontrado")
                case 2:
                    arch = input("ingresa el nombre del archivo: ")
                    ruta_nueva = Path(ruta_documentos + arch + ".html")
                    ruta_nueva.touch(exist_ok=True)
                    with open(ruta_nueva, "+a") as archivo:
                        archivo.write("culo culo" + '\n')
                    print(f"Archivo creado en {ruta_nueva}")
                    continue
        except FileNotFoundError:
            print("Archivo no encontrado")

