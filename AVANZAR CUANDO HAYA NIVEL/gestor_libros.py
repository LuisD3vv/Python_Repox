import time
from os import path
from utils import creacion_isbn
from pathlib import Path

# No usar mkdir cuando la ruta termine en un archivo.
#Crear el archivo si no extiste
rutaFolder = Path("Libros")


def verificar_ruta(ruta):
    """
    Funcion para verificar si existe la ruta, es decir el directorio libros
    y el archivo donde se van a crear, en caso de que no, se crearan
    """
    if ruta.exists():
        print("Ruta existente \U0001F54A.")
    elif not ruta.exists():
        print("Carpeta no encontrada")
        ruta.mkdir(parents=True, exist_ok=True)
        # si alguna carpeta del camino no existe se crea con parents = true, y con exist, si el archhivo
        # ya existe no se lanza error
        time.sleep(2)
        print("Creando carpeta...")
        time.sleep(2)
        print("Carpeta creada")
        # Crear archivo
    archivo = rutaFolder / "Libros.txt"
    archivo.touch(exist_ok=True)
    return archivo


class Libro:
    prestado = False
    """Clase en la que definimos la estructura de cada libro"""
    def __init__(self, titulo, autor, fecha, isbn, genero, editorial):
        self.titulo = titulo
        self.autor = autor
        self.detalles = {
            "fecha": fecha,
            "isbn": isbn,
            "genero": genero,
            "editorial": editorial
        }
    def __str__(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Fecha: {self.detalles['fecha']} | ISBN: {self.detalles['isbn']} | Editorial: {self.detalles['editorial']}"

    def buscar_libro(self):
        ...

    #Property es para obtener los datos almacenados en la variable y regresarlo de manera oculta, tambien es una forma diferente dela habitual al getter
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo_nuevo):
        if len(titulo_nuevo) > 100:
            print("El texto es demaciado largo")
        else:
            self._titulo = titulo_nuevo
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, autor_nuevo):
        if not isinstance(autor_nuevo,str):
            print("Ingresa un nombre valido")
        else:
            self._autor = autor_nuevo
    @property
    # utilizar metodos como atributos, es decir, al momento de llamarlos no necesitaremos parentesis, solo un objeto.atributo
    def fecha(self):
        return self.detalles["fecha"]
    @fecha.setter
    def fecha(self, fecha_nuevo):
        try:
            sep = fecha_nuevo.split("-")
        except ValueError:
            print("Ingresa la fecha completa")
        else:
            anio, mes, dia = sep
            if int(anio) > 2999 or int(anio) < 0000:
                print(f"mamon, como vas a tener esa edad {anio}")
            elif int(mes) > 12 or int(mes) < 0:
                print(f"Ingresa un numero dentro del rango {mes}")
            elif int(dia) <= 0 or int(dia) > 31:
                print(f"dia fuera del rango {dia}")
            else:
                self.detalles["fecha"] = fecha_nuevo

def agregar_libro(titulo,autor,fecha,genero,editorial):
    """Comprobar las entradas del usuario y agregar correctamente el libro"""

    titulo_libro = titulo
    autor_libro = autor
    gen_isb = creacion_isbn()
    detalle = ({
        "fecha": fecha,
        "isbn": gen_isb,
        "genero": genero,
        "editorial": editorial
    })

    # verificar que todas las opciones sean correctas antes de crear el objeto
    objeto = Libro(titulo=titulo_libro, autor=autor_libro, **detalle)
    # el asterico en detalle, es un desempaquetado especial de diccionario clave, valor, si donde queremos sobreescribir los mismos datos, se nombraran como tal
    # es decir, se acoplaran solos
    ruta_libro = verificar_ruta(rutaFolder)
    with open(ruta_libro, "a") as lerbo:
        try:
            lerbo.writelines(str(objeto) + "\n")
        except FileNotFoundError:
            print(f"No se encontro el archivo final de la ruta {ruta_libro}")
        else:
            print("EL libro se anadio exitosamente")

    return objeto

# libro_nuevo = agregar_libro()
# print("Libro nuevo creado")
#
# todos_los_libros = []
# todos_los_libros.append(libro_nuevo)