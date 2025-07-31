import os  # Manipular directorios y archivos del sistema.
import shutil # poder eliminar y realizar operaciones de alto nivel
import time
from os import system
from pathlib import Path  # Manipular y crear rutas

"""
    Author Luis Alejandro Aguilar Soberanes | Lissandro El crack...
    
    Motivo- Recetario con opciones multiples
    -Uso, practicar y conocer las diferentes funciones 
    para manipular archivos, ya sea creandolos o eliminandolos
    asi mismo crear rutas absolutas y relativas a ella.
    tambien utilizar metodos de ellas como de os tanto como de path
"""

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

Nombre = input("Cual es tu nombre crack: ")
# Snippet para comprobar el sistema operativo
if os.name == "nt":
    print("sistema Windows detectado")
elif os.name == "posix":
    print("Sistema Linux detectado")

siRecetasExiste = Path("Udemy/DIA 6 - Rutas y gestion archivos/Recetas") # queremos comprobar que exista la carpeta RECETAS
if not siRecetasExiste.exists():
    siRecetasExiste.mkdir(parents=True,exist_ok=True)
    print("Se ha el directorio Recetas")
else:
    time.sleep(2)
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

def leer_receta(opcion, archivos):
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

def crear_Receta(categoria, rec):
    print(listar_cate(ruta))
    categoria2 = input("Escribe el nombre de la categoria donde te gustaria añadir tu receta: ")
    print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria2}'.")
    archivos2 = listar_dir(categoria2)
    print(*archivos2, sep=", ")
    crear_rec = input("¿Te gustaria crear una receta aqui?:(si-no) ")
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

def crear_categoria(nombre_categoria):
    """Funcion para crear una categoria"""
    system("clear")
    print("Has elegido crear una categoria")
    NombreCategoria = input("Nombre de la categoria: ")
    Categoria_nueva = ruta.joinpath(NombreCategoria)
    # Crear la categoría si no existe, y si existe no mostrar errores fatales
    Categoria_nueva.mkdir(parents=True, exist_ok=True)  # Crear directorio y evitar error si ya existe(con el exist ok, se evita el mensaje de filerror)
    print(f"Categoria '{nombre_categoria}' creada exitosamente.")

def eliminar_Receta(nombre_receta):
    print("Has seleccionado eliminar receta")
    print(listar_cate(ruta))
    categoria3 = input("Selecciona la categoria donde esta la receta: ")
    # Verificar si la categoria está en los directorios
    print(f"Aqui tienes las recetas disponibles de la categoria: '{categoria3}'.")
    archivos3 = listar_dir(categoria3)
    if len(archivos3) == 0:
        print("Esta categoria aun no tiene recetas")
    print(*archivos3, sep=", ")
    eliminarReceta = input("¿Cual receta te gustaria eliminar? ")
    rutita = Path("C:/Users/HP/PycharmProjects/Python_Repox/Code/DIA6/Recetas") / categoria3 / nombre_receta
    if rutita.exists():  # comprobar si la ruta o destino final existe
        rutita.unlink()  # nos sirve para eliminar un archivo seleccionado
        return f"Se ha eliminado la receta => {nombre_receta}"
    else:
        return "Al parecer no existe"

def eliminar_categoria(nombre_categoria):
    """Recibe el nombre por parametro y se elimina"""
    print("Has seleccionado eliminar una categoria")
    print(listar_cate(ruta))
    nombreCategoria = input("Selecciona la categoria que deseas eliminar: ")
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

def modificar_receta():
    print("Que deseas modificar")
    modify = int(input("1.-Cambiar el nombre de la nota\n2.-Cambiar el contenido"))
    if modify == 1:
        print("cambiar el nombre")
    elif modify == 2:
        print("Modificar el contenido")

# Diccionario de funciones, lo utilizar proximamente
funciones = {
        "1": leer_receta,
        "2": crear_Receta,
        "3": crear_categoria,
        "4": eliminar_Receta,
        "5": eliminar_categoria,
        "6": modificar_receta
}

def enviar_mensaje(mensaje, opcion):
    ...

def main():
    system("clear")
    print(f"Numero de Recetas disponibles: |-{archivos_txt}-|")
    while True:
        print(f"Bienvenido {Nombre},Que deseas realizar?")
        try:
            print("1-Leer receta\n"
                  "2-Crear receta\n"
                  "3-Crear categoria\n"
                  "4-Eliminar receta\n"
                  "5-Eliminar categoria\n"
                  "6-Modificar receta\n"
                  "7-Salir"
                  )
            opcion = int(input("Opcion: "))
        except ValueError:
            system("clear")
            print("| Es necesario que ingreses un numero |")
        else:
            match opcion:
                case 1: leer_receta()
                case 2: crear_Receta()
                case 3: crear_categoria()
                case 4: eliminar_Receta()
                case 5: eliminar_categoria()
                case 6: modificar_receta()
                case 7:
                    system("clear")
                    print("Has salido exitosamente")
                    exit()  # Salida logica de todo el codigo
main()