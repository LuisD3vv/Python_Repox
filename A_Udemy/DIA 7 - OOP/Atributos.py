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
    Atributos de clase, todos los objetos por defecto lo tendran
    Atributos de instancia, propios de cada uno
    Los de instancia propios del
    objeto mismo, diferente color,raza,etc 
    pero que siguen compartiendo caracteristicas generales,
    las cuales son las instancias de clase
"""

class Cubo: 
    caras = 6 # atributo de clase, todos los objetos lo tienen por defecto
    def __init__(self, color):
        self.color = color # atributos de instancia, cada objeto puede tener su propia caracteristica
cubo_rojo = Cubo("rojo")


class Personaje:
    real = False # Atributo de clase, todos los objetos lo tienen por defecto
    def __init__(self, especie, magico, edad):
        self.especie = especie # atributos de instancia, puede variar de acuerdo a cada objeto
        self.magico = magico
        self.edad  = edad

# Ejemplo, objeto con sus propias catacteristicas pero mantine el real = false
harry_potter = Personaje("Humano", True, 17)
