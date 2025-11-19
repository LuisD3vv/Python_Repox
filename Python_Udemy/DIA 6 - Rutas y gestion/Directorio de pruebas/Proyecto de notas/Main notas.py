# Gestionador de notas
import os
from pathlib import Path

opcion = int(input(
        "Administrado de Notas\n1. Crear nota\n"
        "2. ver notas\n3. Leer notas\n"
        "4. Eliminar nota\n"
        "5. Salir\n"))


ruta = os.path.join(os.path.dirname(__file__),'notas/')
print(f"Ruta actual es {ruta}")
os.system("clear")
while True:
    print(f"Numero de Notas disponibles: [{len(os.listdir(ruta))}]")
    if opcion == 1:
        print("Has seleccionado crear nota")
        nombre_nota = input("Nombre de la nota: ")
        if os.path.exists(ruta / nombre_nota + ".txt"):
            print('Ya existe una nota con ese nombre, elige otro nombre.')
            continue
        else:
            with open(ruta / nombre_nota , "w") as nota:
                print("Escribe tu nota abajo (cuando termines, escribe 'FIN') ")
                lineas = []
                while True:
                    linea = input()
                    if linea.upper() == "FIN":
                        contenido = "\n".join(lineas)
                        nota.write(contenido)
                        print("Nota creada con exito")
                        break

    elif opcion == 2:
        print("Has seleccionado ver notas")
        notas_disponibles = os.listdir(ruta)
        for i in notas_disponibles:
            print(i.removesuffix(".txt"))
    elif opcion == 3:
        print("Has seleccionado leer notas")
        notas_disponibles = os.listdir(ruta)
        for i in notas_disponibles:
            print(i.removesuffix(".txt"))
        leer_nota = input("Ingresa el nombre de la receta: ")
        if not leer_nota.endswith(".txt"):
            leer_nota += ".txt"

        print(f"El nombre de la nota es: {leer_nota}")
        if leer_nota in notas_disponibles:
            with open(ruta / leer_nota, "r") as nota:
                print(nota.read())
        else:
            print("Ingresa el nombre de la nota correctamente")
    elif opcion == 4:
        print("Has seleccionado eliminar nota")
    elif opcion == 5:
        print("Has salido exitosamente")
    exit()

# Pasos clave para tu Administrador de Notas:
# 1. Crear carpeta notas/ si no existe
#
# import os
#
# if not os.path.exists("notas"):
#     os.mkdir("notas")
#
# 2. Crear una nota
#
#     Pide título y contenido.
#
#     Guarda en notas/{titulo}.txt.
#
# 3. Ver notas disponibles
#
#
#
# 4. Leer una nota
#
#     Pide el nombre.
#
#     Abre y muestra su contenido.
#
# 5. Eliminar una nota
#
#     Pide el nombre.
#
#     Usa os.remove() para borrarla.