class Pajaro:
   alas = True # todos los objetos tienen este valor
   def __init__(self, color,  especie):# Contructor de la clase
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro("negro", "culo")

print(f" mi pajaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")# Instancia de clase

# Estos son ejemplos de atributos de instacia 

# existen dos tipos de atributos

""""
Atributos de clase
Atributos de instancia
#Los de instancia propios del objeto mismo, diferente color,raza,etc pero que siguen compartiendo caracteristicas generales.
"""
class Cubo: 
    caras = 6 # atributo de clase, todos los objetos lo tienen por defecto
    def __init__(self, color):
        self.color = color # atributos de instancia
        

cubo_rojo = Cubo("rojo")


class Personaje:
    real = False # Instancia de clase, todos los objetos lo tienen por defecto
    def __init__(self, especie, magico, edad):
        self.especie = especie # atributos de instancia
        self.magico = magico
        self.edad  = edad
    
harry_potter = Personaje("Humano", True, 17)