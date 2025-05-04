import os  # Manipular directorios y archivos del sistema.
from pathlib import Path  # Manipular y crear rutas


if os.name == "nt":
    print("Estas en un sistema Windows")
elif os.name == "posix":
    print("Estas en un sistema Linux")

ruta = Path.home() / "PycharmProjects" / "Python_Repox" / "Code" / "DIA6" / "Recetas"
print(ruta)

# Contar los archivos
archivos_txt = 0

# Iteracion para buscar recursivamente dentro de subcarpetas, con ayuda del os.walk()
for carpeta, subcarpeta, archivos in os.walk(ruta):
    archivos_txt += sum(1 for archivos in archivos if archivos.endswith(".txt"))

# Imprimiendo La primera parte
print(f"Bienvenido, La carpeta recetas se encuentra en la siguiente ruta [{ruta}]")
print(f"Numero de Recetas disponibles inicialmente: [-{archivos_txt}-]")

cate = os.listdir(ruta)

def listar_dir(categoria):
    return os.listdir(ruta / categoria)


while True:
    print(f"Numero de Recetas disponibles: [-{archivos_txt}-]")
    opcion = int(input(
        "Que deseas realizar\n1-Leer Recetas\n"
        "2-Crear Receta\n3-Crear categoria\n"
        "4-Eliminar receta(s)\n"
        "5-Eliminar Categoria\n"
        "6-Salir\n"))

    if opcion == 1:
        print(f"Categorias disponibles -> [{" ".join(cate)}] ")

        print("Selecciona la categoria de tu interes para leer:")

        categoria = input("Selecciona escribiendo el nombre de la categoria: ")

        archivos = listar_dir(categoria)

        archivos_sinex = [Path(a).stem for a in archivos]

        print(*archivos_sinex, sep=", ")

        leer = (input("¿Deesas leer alguna?:(si-no) "))

        if leer == "si":
            opcion_leer = input("Escribe aqui cual deseas leer: ")
            opcion_leer_ext = opcion_leer + ".txt"  # colocar txt de nuevo con fines de busquda.

            if opcion_leer_ext in archivos:
                print("Aqui tienes la receta de:", opcion_leer)
                with open(ruta / categoria / opcion_leer_ext, "r") as lec:
                    print(lec.read())
            elif leer == "no":
                continue
        else:
            print("Intenta de nuevo")

        # Este es el codigo para crear recetas.
    elif opcion == 2:
        print(f"Categorias disponibles -> [{" ".join(cate)}] ")
        categoria2 = input("Escribe el nombre de la categoria donde te gustaria añadir tu receta: ")

        # Verificar si la categoria está en los directorios
        print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria2}'.")
        archivos2 = listar_dir(categoria2)
        print(*archivos2, sep=", ")
        crear_rec = input("¿Te gustaria crear una receta aqui?:(si-no) ")

        if crear_rec == "si":
            nombre_receta = input("Como se llama la receta?:")

            if not nombre_receta.endswith(".txt"):
                nombre_receta += ".txt"

                with open(ruta / categoria2 / nombre_receta, "w") as c:
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
    # Creacion de carpetas(Categorias)
    if opcion == 3:
        print("Has elegido crear una categoria")
        NombreCategoria = input("Nombre de la categoria: ")
        Categoria_nueva = ruta / NombreCategoria
        # Crear la categoría si no existe
        Categoria_nueva.mkdir(parents=True, exist_ok=True)  # Crear directorio y evitar error si ya existe
        print(f"Categoria '{NombreCategoria}' creada exitosamente.")

    if opcion == 4:
        print("Has seleccionado eliminar receta")
        print(f"Categorias disponibles -> [{" ".join(cate)}] ")
        categoria3 = input("Selecciona la categoria donde esta la receta: ")

        # Verificar si la categoria está en los directorios
        print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria3}'.")
        archivos3 = listar_dir(categoria3)
        print(*archivos3, sep=", ")
        eliminar_receta = input("¿Cual receta te gustaria eliminar? ")

        rutita = Path("C:/Users/HP/PycharmProjects/Python_Repox/Code/DIA6/Recetas") / categoria3 / eliminar_receta
        if rutita.exists():
            rutita.unlink()  # nos sirve para eliminar
            print("Se ha eliminado la receta", eliminar_receta)
        else:
            print("Al parecer no existe")
    if opcion == 5:
        print("Se esta trabajando")
    # os.rmdir('ruta') eliminar directorio util para el proyecto 6
    elif opcion == 6:
        print("Has salido")
        exit()
        #Salir de todo el codigo

""""
Cuando el codigo este finalizado, 
favor de mejorarlo con la implementacion de funciones.
"""
