class Usuario:
    """Clase para definir la estructura de cada usuario"""
    def __init__(self,nombre,user_id,edad):
        self.nombre = nombre
        self.edad = edad # Para prohibir ciertos titulos
        self.user_id = user_id



def registrar_usuarios():
    ...
    
def buscar_usuario():
    ...
    
def listar_usuarios():
    ...

#Usar map() para mostrar títulos en mayúscula

#Usar filter() para buscar por año
