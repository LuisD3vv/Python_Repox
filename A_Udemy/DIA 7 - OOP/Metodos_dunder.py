# mi_lista = [1,1,1,1,1,1,1]
# print(mi_lista)
# class Objeto:
#     ...
# mi_objeto = Objeto()
# print(mi_objeto)

class CD:
    """
    Clase de prueba para conocer los metodos dunder
    """
    def __init__(self, autor, titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    #metodo str, definir como se veran los metodos al ser solicitados, hay muchos mas
    def __str__(self):
        return f"Album: '{self.titulo}' de {self.autor}"
    def __len__(self):
        return self.canciones
    def __del__(self):
        print(f"Se ha elimando correctamente [-{self}-]") # Muestra el libro eliminado
    def __getitem__(self):
        print(self)
mi_cd = CD('Queen', 'The game', 15)

print(mi_cd)
print(len(mi_cd))


#Eliminar instancia
del mi_cd

# 
class MiLista:
    def __init__(self):
        self.data = []
        
    def __getitem__(self,indice): # Acceso a indices
        return self.data[indice]
    
    def __setitem__(self,index,valor):# modificar un indices
        self.data[index] = valor
        
    def __delitem__(self,item):# eliminar un indice
        del self.data[item]
    
Mi_lista = MiLista()
Mi_lista.data = [1,2,3,4,5,6,7,8,9,10]
print(Mi_lista[2])
Mi_lista[2] = 30
print(Mi_lista[2])
del Mi_lista[2]
print(Mi_lista.data)

# Ejemplo con __eq__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.nombre == other.nombre and self.edad == other.edad
        return False

p1 = Persona("Lissandro", 25)
p2 = Persona("Lissandro", 25)
p3 = Persona("Otro", 25)
"""
__ne__ → Not equal !=

__lt__ → Less than <

__le__ → Less or equal <=

__gt__ → Greater than >

__ge__ → Greater or equal >=
"""
print(p1 == p2)  # ✅ True
print(p1 == p3)  # ❌ False


"""
Necesitamos crear nuevos metodos dentro de nuestras clases para
configurar correctamente el funcionamiento de estas
"""
