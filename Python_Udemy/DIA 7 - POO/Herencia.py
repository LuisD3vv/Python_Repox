class Animal:
    vertebrado = True
    def __init__(self,edad,color):
        """Atributos de instancia"""
        self.edad = edad
        self.color = color
    def nacen(self):
        print("Este animal ha nacido")


class Pajaro(Animal): # Se le pasa como parametro el nombre de la clase para heredar
    """
    Pajaro recibe los atributos de Animal, ya sean 
    de instancia o clase, eso no quita que podamos 
    modificar los atributos ya establecidos
    """

Piolin = Pajaro(2,"Amarillo")
Piolin.nacen()

# Comprobar la clase y a que padre pertenece el hijo
print(Animal.__subclasses__()) # subclases del padre
print(Pajaro.__base__) # Conocer padre

print(Piolin.color)

##Ejercicios para visualizar mejor lo que hicimos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Alumno(Persona):
    ...


# Tambien funciona con metodos

class Vehiculo:
    def acelerar(self):
        ...
    def frenar(self):
        ...
        
class Automovil(Vehiculo):
    """Automovil Hereda los metodos de la clase
    vehiculo, haciendo que cualquier objeto
    de automovil pueda utilizarlos
    """
    ...
