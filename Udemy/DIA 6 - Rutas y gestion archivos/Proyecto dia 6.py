import os  # Manipular directorios y archivos del sistema.
import shutil # poder eliminar y realizar operaciones de alto nivel
from os import system
from pathlib import Path  # Manipular y crear rutas

"""
Author Luis Alejandro Aguilar Soberanes | Lissandro El crack...

Motivo- Rectetario
-Uso, practicar y conocer las diferentes funciones 
para manipular archivos, ya sea creandolos o eliminandolos
asi mismo crear rutas absolutas y relativas a ella.
tambien utilizar metodos de ellas como de os tanto como de path
"""
Nombre = input("Cual es tu nombre crack: ")
# Snippet para comprobar el sistema operativo
if os.name == "nt":
    print("Estas en un sistema Windows")
elif os.name == "posix":
    print("Estas en un sistema Linux")

siRecetasExiste = Path("Udemy/DIA 6 - Rutas y gestion archivos/Recetas") # queremos comprobar que exista la carpeta RECETAS
if not siRecetasExiste.exists():
    siRecetasExiste.mkdir(parents=True,exist_ok=True)
    print("Se ha el directorio Recetas")
else:
    print("Iniciando...")
# Sitemas de ruta principal, que toma como base la ruta base del sistema operativo
ruta = Path.home() / "Python_Repox/Udemy/DIA 6 - Rutas y gestion archivos/Recetas"
print(f"La ruta es la siguiente: {ruta}")
# Contar los archivos
archivos_txt = 0

# Iteracion para buscar recursivamente dentro de subcarpetas, con ayuda del os.walk(, necesita 3 parametros
for carpeta, subcarpeta, archivos in os.walk(ruta):
    archivos_txt += sum(1 for archivos in archivos if archivos.endswith(".txt"))
"""
Archivos
el uso de dos 3 indices dentro de del ciclo,
es debido a los requerimientos de la propia funcion walk del modulo os,
la cual nos pide (dirpath, dirnames, filenames)
cada una es un nivel del directorio al cual queremos aplicarle la busqueda recursiva dentro de sus directorios y subdirectorios.
"""

# Imprimiendo La primera parte
print(f"Bienvenido, La carpeta recetas se encuentra en la siguiente ruta [{ruta}]")

# Regresa un listado de las rutas que hay dentro de la carpeta padre Recetas
def listar_cate(ruta):
    return os.listdir(ruta)


def listar_dir(aelegir):
    for indice, valor in enumerate(os.listdir(ruta)):
        if indice == aelegir:
            return os.listdir(ruta/valor)

def leer_receta(opcion,archivos):
    leer = input("¿Deesas leer alguna?[si-no]: ")
    """Funcion para leer la eleccion del usuario"""
    if leer == "si":
        opcion_leer = input("Escribe aqui cual deseas leer: ")
        opcion_leer += ".txt"  # colocar txt de nuevo con fines de busquda.
        if opcion_leer in archivos:
            print("Aqui tienes la receta:", opcion_leer)
            with open(ruta / opcion / opcion_leer, "r") as lec: # con la ruta, categoria y el archivo seleccionado previamente, lee este
                print(lec.read())
    elif leer == "no":
        pass
    else:
        print("Intenta de nuevo")

def Crear_Receta(categoria,rec):
    if rec == "si":
        receta = input("Como se llama la receta?:")
        if not receta.endswith(".txt"):
            receta += ".txt"
            # Gracias a este codigo podemos introducir multiples lineas y hacer mas legible al escribir una receta.
            with open(ruta / categoria / receta, "w") as c:
                print("Abajo escribe la receta (cuando termines, escribe 'FIN') ")
                lineas = [] # Lineas se declara en blanco
                while True: # mientras la condicion no se cumpla se seguira ejecutando
                    linea = input() # Un input en blanco
                    if linea.upper() == "FIN": #Esta es la condicion para detener el bucle, una linea que diga fin
                        break
                    lineas.append(linea) #Agregamos la linea a la lista
                contenido = "\n".join(lineas) # al final, el contenido de,"contenido" seran las lineas unidas por saltos de linea(suena raro pero asi es)
                c.write(contenido) # Aqui guardamos lo escrito en el archivo de texto que es la receta
                print("Tu receta se creo exitosamente!!")
        else:
            print("La receta ya existe.")
    elif crear_rec == "no":
            pass
    else:
        print("Intenta de nuevo")
def Crear_categoria(nombre_categoria):
    """Funcion para crear una categoria"""
    Categoria_nueva = ruta / nombre_categoria
    # Crear la categoría si no existe
    Categoria_nueva.mkdir(parents=True, exist_ok=True)  # Crear directorio y evitar error si ya existe(con el exist ok, se evita el mensaje de filerror)
    print(f"Categoria '{nombre_categoria}' creada exitosamente.")
def Eliminar_Receta(nombre_receta):
    rutita = Path("C:/Users/HP/PycharmProjects/Python_Repox/Code/DIA6/Recetas") / categoria3 / nombre_receta
    if rutita.exists():  # comprobar si la ruta o destino final existe
        rutita.unlink()  # nos sirve para eliminar un archivo seleccionado
        return f"Se ha eliminado la receta => {nombre_receta}"
    else:
        return "Al parecer no existe"
def Eliminar_categoria(nombre_categoria):
    """Recibe el nombre por parametro y se elimina"""
    eliminarCategoria_ruta = ruta / nombre_categoria

    eleccion = input("¿Estas seguro de elimnar esta categoria?: ")

    if eleccion == "si":
        if os.path.exists(eliminarCategoria_ruta): # si la ruta existe
            print(f"Categoria {nombre_categoria} Eliminada exitosamente")
            shutil.rmtree(eliminarCategoria_ruta, ignore_errors=True) # eliminar un arbol de directorios, es decir un directorio y su contenido, mas aparte ignorara los errores.
        else:
            print("Proporciona una ruta valida")
    else:
        pass
system("clear")
print(f"Numero de Recetas disponibles: |-{archivos_txt}-|")
while True:
    print(f"Bienvenido {Nombre},Que deseas realizar?")
    try:
        opcion = int(input(
            "1.-Leer Recetas\n"
            "2.-Crear Receta\n3.-Crear categoria\n"
            "4.-Eliminar receta(s)\n"
            "5.-Eliminar Categoria\n"
            "6.-Modificar receta\n"
            "7-Salir\n"))
    except ValueError:
        system("clear")
        print("| Es necesario que ingreses un numero |")
    else:
        if opcion == 1:
            print("Categorias Disponibles")
            for elemento in enumerate(os.listdir(ruta)): # iterar sobre los elementos de una ruta
                print(*elemento)
            try:
                categoria = int(input("Selecciona la de tu preferencia: "))
                archivos = listar_dir(categoria)
                archivos_sinex = [Path(a).stem for a in archivos] # por cada elemento en archivos, se le quiatara el stem(extension jpg,pdf,txt)
                print(*archivos_sinex, sep=", ") # Separar las opciones con comas
            except FileNotFoundError:
                print("El directorio ingresado no existe, porfavor ingresa uno existente o crea uno.")
            else:
                leer_receta(categoria,archivos)
        # Este es el codigo para crear recetas.
        elif opcion == 2:
            print(listar_cate(ruta))
            categoria2 = input("Escribe el nombre de la categoria donde te gustaria añadir tu receta: ")
            print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria2}'.")
            archivos2 = listar_dir(categoria2)
            print(*archivos2, sep=", ")
            crear_rec = input("¿Te gustaria crear una receta aqui?:(si-no) ")
            Crear_Receta(categoria2,crear_rec)
            # Creacion de carpetas(Categorias)
        elif opcion == 3:
            system("clear")
            print("Has elegido crear una categoria")
            NombreCategoria = input("Nombre de la categoria: ")
            Crear_categoria(NombreCategoria)
        elif opcion == 4:
            print("Has seleccionado eliminar receta")
            print(listar_cate(ruta))
            categoria3 = input("Selecciona la categoria donde esta la receta: ")
            # Verificar si la categoria está en los directorios
            print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria3}'.")
            archivos3 = listar_dir(categoria3)
            if len(archivos3) == 0:
                print("Esta categoria aun no tiene recetas")
                break
            print(*archivos3, sep=", ")
            eliminarReceta = input("¿Cual receta te gustaria eliminar? ")
            print(Eliminar_Receta(eliminarReceta))
        elif opcion == 5:
            print("Has seleccionado eliminar una categoria")
            print(listar_cate(ruta))
            nombreCategoria = input("Selecciona la categoria que deseas eliminar: ")
            print(Eliminar_categoria(nombreCategoria))
        elif opcion == 6:
            print("Que deseas modificar")
            modify = int(input("1.-Cambiar el nombre de la nota\n2.-Cambiar el contenido"))
            if modify == 1:
                print("cambiar el nombre")
            elif modify == 2:
                print("Modificar el contenido")
        elif opcion == 7:
            system("clear")
            print("Has salido exitosamente")
            exit()  # Salida logica de todo el codigo


"""
Funciones y librerias utilizadas:
    import os  # Manipular directorios y archivos del sistema.
    import shutil # poder eliminar y realizar operaciones de alto nivel, como borrar directorios con contenido
    from pathlib import Path  # Manipular y crear rutas
shutil se usa para operaciones de alto nivel con archivos y directorios, como:

    Copiar (shutil.copy, copytree)

    Mover (shutil.move)

    Borrar (shutil.rmtree)

    Hacer archivos comprimidos (make_archive)
"""
