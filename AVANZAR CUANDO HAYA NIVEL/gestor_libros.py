from utils import creacion_isbn
from pathlib import Path

ruta = Path("AVANZAR CUANDO HAYA NIVEL/Libros/Libro.txt")

class Libro:
    """Clase en la que definimos la estructura de cada libro"""
    
    # Crear donde verga se van a guardar los libros alv jaja
    def __init__(self,titulo,autor,fecha,isbn,genero,editorial):
        self.titulo = titulo
        self.autor = autor
        self.detalles = {
            "fecha": fecha,
            "isbn": isbn,
            "genero": genero,
            "editorial": editorial
        }
    def __str__(self):
        return f" Detalles del libro\nTitulo: {self.titulo} | Autor: {self.autor} | Fecha: {self.detalles["fecha"]} | ISBN: {self.detalles["isbn"]} | Editorial {self.detalles["editorial"]}"
    
    @staticmethod
    def buscar_libro(self):
        ...

    #Property es para obtener le datos almacenados en la variable y regresarlo de manera oculta, tambien es una forma diferente dela habitual al getter
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,titulo_nuevo):
        if len(titulo_nuevo) > 100:
            print("El texto es demaciado largo")
            self._titulo = None
        else:
            self._titulo = titulo_nuevo
            return "formato titulo correcto"
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self,autor_nuevo):
        if not isinstance(autor_nuevo,str):
            print("Ingresa un nombre valido")
            self._autor = None
        else:
            self._autor = autor_nuevo
            return  "formato autor correcto"
    @property # utilizar metodos como atributos, es decir, al momento de llamarlos no necesitaremos parentesis, solo un objeto.atributo
    def fecha(self):
        """getter
        utilizando esto, aunque el objeto este dentro
        de un diccionario, podremos acceder a el mediante
        libro.fecha como tal
        """
        return self.detalles["fecha"]
    @fecha.setter
    def fecha(self,fecha_nuevo):
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
    gen_isb =  creacion_isbn()
    detalle = ({
        "fecha": fecha,
        "isbn":gen_isb,
        "genero": genero,
        "editorial": editorial
    })
    
    # verificar que todas las opciones sean correctas antes de crear el objeto
    objeto = Libro(titulo=titulo_libro,autor=autor_libro,**detalle)
    # el asterico en detalle, es un desempaquetado especial de diccionario clave, valor, si donde queremos sobreescribir los mismos datos, se nombraran como tal
    # es decir, se acoplaran solos
    with open(ruta,"a") as lerbo:
        lerbo.writelines(f"Titulo: {titulo} | Autor: {autor} | Fecha: {detalle["fecha"]} | ISBN: {detalle["isbn"]}\n")
        print("Registro exitoso")
        
    print("Libro correctamente agregado")
    return "El libro añadio correctamente"


print(Libro.__subclasses__)


# def buscar_por_titulo():
#     ...
    
# def buscar_por_autor():
#     ...
    
# def listar_libros():
#     ...
