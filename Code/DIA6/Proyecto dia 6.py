import os
from os import system
from pathlib import Path

# Creando la ruta absoluta
directorio = Path("/home/lissandro/Escritorio/Recetas/Recetas")

# Contar los archivos
archivos_txt = 0

# Iteracion para buscar recursivamente dentro de subcarpetas, con ayuda del os.walk()
for carpeta, subcarpeta, archivos in os.walk(directorio):
    archivos_txt += sum(1 for archivos in archivos if archivos.endswith(".txt"))

'''
Alternativa con Path

# Ruta del directorio
directorio = Path('ruta/del/directorio')

# Contar archivos .txt de manera recursiva
archivos_txt = len(list(directorio.rglob('*.txt')))
'''
# Imprimiendo La primera parte
print(f"Bienvenido,recetas se encuentra en la siguiente ruta [{directorio}]")
print(f"El numero de Recetas disponibles por el momento es de: {archivos_txt}")


# Borrador de funcionamiento.
while True:
    opcion = int(input(
            "Deseas realizar algo mas\n1-Leer Recetas\n2-Crear Receta\n3-Crear categoria\n4-Eliminar receta(s)\n5-Eliminar Categoria\n6-Salir\n"))

    if opcion == 1:
        print("Categorias disponibles:")
        categoria = input("Estas son nuestras categorias disponibles\n1-Carnes\n2-Ensaladas\n3-Pastas\n4-Postres\n")

        # Directorio general
        directorios = {
            "Carnes": Path("/home/lissandro/Escritorio/Recetas/Recetas/Carnes"),
            "Ensaladas": Path("/home/lissandro/Escritorio/Recetas/Recetas/Ensaladas"),
            "Pastas": Path("/home/lissandro/Escritorio/Recetas/Recetas/Pastas"),
            "Postres": Path("/home/lissandro/Escritorio/Recetas/Recetas/Postres"),
        }
        system("clear")

        if categoria in directorios:
            print(f"Aqui tienes las recetas disponibles de la categoria: {categoria}")
            print("Las recetas disponibles:")
            archivos = os.listdir(directorios[categoria])
            print(archivos)

            leer = int(input("deseas leer alguna?: "))
            if leer == 1:
                with open("/home/lissandro/Escritorio/Recetas/Recetas/Carnes/Entrecot al Malbec.txt","r",encoding="utf-8") as lectura:
                    archivos = lectura.read()
                    print(archivos)
        else:
            print("Intenta de nuevo")


        if opcion == 2:
            print("Categorias disponibles:")
            categoria = input("Estas son nuestras categorias disponibles\n1-Carnes\n2-Ensaladas\n3-Pastas\n4-Postres\n")

            # Directorio general
            directorios = {
                "Carnes": Path("/home/lissandro/Escritorio/Recetas/Recetas/Carnes"),
                "Ensaladas": Path("/home/lissandro/Escritorio/Recetas/Recetas/Ensaladas"),
                "Pastas": Path("/home/lissandro/Escritorio/Recetas/Recetas/Pastas"),
                "Postres": Path("/home/lissandro/Escritorio/Recetas/Recetas/Postres"),
            }
            system("clear")




    elif opcion == 6:
       print("Has salido")
       break
    else:
        print("porfavor ingresa una opcion valida")