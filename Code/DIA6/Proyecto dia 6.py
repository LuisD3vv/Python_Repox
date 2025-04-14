import os # Manipular directorios y archivos del sistema.
from pathlib import Path # Manipular y crear rutas
from pathlib import PureWindowsPath



# Creando la ruta absoluta
directorio = Path("/home/lissandro/Escritorio/Recetas/Recetas")
ruta_windows = PureWindowsPath(directorio)

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
print(f"Bienvenido, La carpeta recetas se encuentra en la siguiente ruta [{directorio}]")
print(f"Numero de Recetas disponibles: {archivos_txt}")

# Directorio general
directorios = {
    "Carnes": Path("/home/lissandro/Escritorio/Recetas/Recetas/Carnes"),
    "Ensaladas": Path("/home/lissandro/Escritorio/Recetas/Recetas/Ensaladas"),
    "Pastas": Path("/home/lissandro/Escritorio/Recetas/Recetas/Pastas"),
    "Postres": Path("/home/lissandro/Escritorio/Recetas/Recetas/Postres"),
}
# Borrador de funcionamiento.
while True:
    opcion = int(input(
            "Que deseas realizar\n1-Leer Recetas\n2-Crear Receta\n3-Crear categoria\n4-Eliminar receta(s)\n5-Eliminar Categoria\n6-Salir\n"))

    if opcion == 1:
        print("Selecciona la categoria de tu interes para leer:")
        print("Categorias disponibles\n.--Carnes\n.--Ensaladas\n.--Pastas\n.--Postres\n")
        categoria = input("Selecciona escribiendo el nombre de la categoria: ")

        # Verificar  si la categoria esta en los directorios
        if categoria in directorios:
            print(f"Recetas disponibles de la categoria: {categoria}")
            archivos = os.listdir(directorios[categoria])
            archivos_sinex = [Path(a).stem for a in archivos] #Quitar .txt
            print(*archivos_sinex, sep=", ")

            # Si selecciono alguna categoria, mostrar las recetas disponibles en esa carpeta
            leer = (input("¿Deesas leer alguna?: "))

            if leer == "si":
             opcion_leer = input("Escribe aqui cual deseas leer: ")
             opcion_leer_ext = opcion_leer + ".txt" # colocar txt de nuevo con fines de busquda.

             if opcion_leer_ext in archivos:
                print("Aqui tienes la receta de:", opcion_leer)
                op = Path(directorios[categoria]) / opcion_leer_ext #guardar la direccion de la ruta y categoria, buscar solamente la coincidencia dentro.
                with open(directorios[categoria] / op, "r") as lec:
                    print(lec.read())
            elif leer == "no":
                continue
        else:
            print("Intenta de nuevo")


        # Este es el codigo para crear recetas.
    elif opcion == 2:
        print("Estas son nuestras categorias disponibles\n--Carnes\n--Ensaladas\n--Pastas\n--Postres\n")
        categoria2 = input("Escribe el nombre de la categoria donde te gustaria añadir tu receta: ")

        # Verificar  si la categoria esta en los directorios
        if categoria2 in directorios:
            print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria2}'.")
            archivos2 = os.listdir(directorios[categoria2])
            print(*archivos2, sep=", ")
        crear_rec = input("¿Te gustaria crear una receta aqui?: ")

        if crear_rec == "si":
            nombre_receta = input("Como se llama la receta?:")

            if not nombre_receta.endswith(".txt"):
                nombre_receta += ".txt"

            if not os.path.exists(nombre_receta):
                with open(directorios[categoria2] / nombre_receta, "w") as c:
                    print("Abajo escribe la receta (cuando termines, escribe 'FIN') ")
                    lineas = []
                    while True:
                        linea = input()
                        if linea.upper() == "FIN":
                            break
                        lineas.append(linea)
                    contenido = "\n".join(lineas)
                    c.write(contenido)
                print("Tu receta se creo exitosamente!!")
            else:
                print("La receta ya existe.")

        elif crear_rec == "no":
            continue
        else:
            print("Intenta de nuevo")


    elif opcion == 6:
        print("Has salido")
        exit()# Salir de todo el codigo
