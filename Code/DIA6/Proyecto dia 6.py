import os  # Manipular directorios y archivos del sistema.
import shutil # poder eliminar y realizar operaciones de alto nivel
from os import system
from pathlib import Path  # Manipular y crear rutas


"""
Author Luis Alejandro Aguilar Soberanes

Motivo- Rectetario


-Uso, practicar y conocer las diferentes funciones para manipular archivos, ya sea creandolos o eliminandolos
asi mismo crear rutas absolutas y relativas a ella.

"""


# Snippet para comprobar el sistema operativo
if os.name == "nt":
    print("Estas en un sistema Windows")
elif os.name == "posix":
    print("Estas en un sistema Linux")

# Sitemas de ruta principal, que toma como base la ruta base del sistema operativo
ruta = Path.home() / "PycharmProjects" / "Python_Repox" / "Code" / "DIA6" / "Recetas"
print(ruta)

# Contar los archivos
archivos_txt = 0

# Iteracion para buscar recursivamente dentro de subcarpetas, con ayuda del os.walk()
for carpeta, subcarpeta, archivos in os.walk(ruta):
    archivos_txt += sum(1 for archivos in archivos if archivos.endswith(".txt"))
"""
:Archivos
el uso de dos 3 indices dentro de del ciclo,
es debido a los requerimientos de la propia funcion walk del modulo os,
la cual nos pide (dirpath, dirnames, filenames)
cada una es un nivel del directorio al cual queremos aplicarle la busqueda recursiva dentro de sus directorios y subdirectorios.
"""

# Imprimiendo La primera parte
print(f"Bienvenido, La carpeta recetas se encuentra en la siguiente ruta [{ruta}]")
print(f"Numero de Recetas disponibles inicialmente: [-{archivos_txt}-]")

# Regresa un listado de las rutas que hay dentro de la carpeta padre Recetas
def listar_cate(ruta):
    return os.listdir(ruta)

def listar_dir(categoria):
    # Esta funcion toma como referencia la categoria que el usuario está buscando, para listarla y regresar el contenido.
    # ... Los tres puntos son iguales que el argumento "pass" para indicarle a una funcion que aún falta el codigo interiori, pero sin afectar slo demás fuera de ella
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
        print(listar_cate(ruta))
        categoria = input("Selecciona escribiendo el nombre de la categoria: ")
        archivos = listar_dir(categoria)
        archivos_sinex = [Path(a).stem for a in archivos] # por cada elemento en archivos, se le quiatara el stem(extension jpg,pdf,txt)
        print(*archivos_sinex, sep=", ") # Separar las opciones con comas

        leer = (input("¿Deesas leer alguna?:(si-no) "))

        if leer == "si":
            opcion_leer = input("Escribe aqui cual deseas leer: ")
            opcion_leer += ".txt"  # colocar txt de nuevo con fines de busquda.

            if opcion_leer in archivos:
                print("Aqui tienes la receta:", opcion_leer)
                with open(ruta / categoria / opcion_leer, "r") as lec: # con la ruta, categoria y el archivo seleccionado previamente, lee este
                    print(lec.read())
            elif leer == "no":
                continue
        else:
            print("Intenta de nuevo")

    # Este es el codigo para crear recetas.
    elif opcion == 2:
        print(listar_cate(ruta))
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
                # Gracias a este codigo podemos introducir multiples lineal y hacer mas legible al escribir una receta.
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
        Categoria_nueva.mkdir(parents=True, exist_ok=True)  # Crear directorio y evitar error si ya existe(con el exist ok, se evita el mensaje de filerror)
        print(f"Categoria '{NombreCategoria}' creada exitosamente.")

    if opcion == 4:
        print("Has seleccionado eliminar receta")
        print(listar_cate(ruta))
        categoria3 = input("Selecciona la categoria donde esta la receta: ")

        # Verificar si la categoria está en los directorios
        print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria3}'.")
        archivos3 = listar_dir(categoria3)
        print(*archivos3, sep=", ")
        eliminarReceta = input("¿Cual receta te gustaria eliminar? ")

        rutita = Path("C:/Users/HP/PycharmProjects/Python_Repox/Code/DIA6/Recetas") / categoria3 / eliminarReceta
        if rutita.exists():  # comprobar si la ruta o destino final existe
            rutita.unlink()  # nos sirve para eliminar un archivo seleccionado
            print("Se ha eliminado la receta", eliminarReceta)
        else:
            print("Al parecer no existe")
    if opcion == 5:
        print("Has seleccionado eliminar una categoria")
        print(listar_cate(ruta))
        eliminarCategoria = input("Selecciona la categoria que deseas eliminar: ")

        eliminarCategoria_ruta = ruta / eliminarCategoria

        eleccion = input("¿Estas seguro de elimnar esta categoria?: ")

        if eleccion == "si":
            if os.path.exists(eliminarCategoria_ruta): # si la ruta existe
                print("Categoria Elimindada exitosamente {}".format(eliminarCategoria))
                shutil.rmtree(eliminarCategoria_ruta, ignore_errors=True) # eliminar un arbol de directorios, es decir un directorio y su contenido, mas aparte ignorara los errores.
            else:
                print("Proporciona una ruta valida")
        else:
            pass

    elif opcion == 6:
        print("Has salido exitosamente")
        exit()  # Salida logica de todo el codigo

""""
Funciones y librerias utilizadas


import os  # Manipular directorios y archivos del sistema.
import shutil # poder eliminar y realizar operaciones de alto nivel, como borrar directorios con contenido
from pathlib import Path  # Manipular y crear rutas

shutil se usa para operaciones de alto nivel con archivos y directorios, como:

    Copiar (shutil.copy, copytree)

    Mover (shutil.move)

    Borrar (shutil.rmtree)

    Hacer archivos comprimidos (make_archive)
"""
