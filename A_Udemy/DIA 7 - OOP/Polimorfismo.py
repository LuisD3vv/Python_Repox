"""
El polimorfismo nos dice que un mismo metodo
puede comportarse de diferentes maneras segun el objeto 
sobre el que este actuando, en funcion de como dicho
metodo ha sido creado, pudiendo compatir el mismo nombre 
pero ejecutando una actividad diferente
"""
class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Muuu")

class Obeja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Meeee")


vaca1 = Vaca('Lala')
Oveja = Obeja('Shaun')


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(Oveja)
# animales = [vaca1, Oveja]

# for animal in animales:
#     animal.hablar()



#Ejercicio de polimorfismo
"""

Cada clase utiliza el mismo nombre de metodo
pero actuan diferente segun el objeto sobre el que se aplican
asi mismo se pueden iterar sobre los elemento que comparten
un mismo nombre de metodo

"""

print("Ataque\n")
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        

Harry_potter = Mago()
Legolas = Arquero()
Jack = Samurai()

personajes = [Legolas,Harry_potter,Jack]

for Personaje in personajes:
    Personaje.atacar() # como cada personaje es un objeto, se le aplica ese metodo

#Tambien en funcion de el objeto que se pasa a una funcion

print("Defensa\n")
class Mago():
    """Mago"""
    def defender(self):
        print("Escudo mágico")

class Arquero():
    """Arquero"""
    def defender(self):
        print("Esconderse")

class Samurai():
    """Samurai"""
    def defender(self):
        print("Bloqueo")

Harry_potter = Mago()
Legolas = Arquero()
Jack = Samurai()


def personaje_defender(lista_objeto):
    for mono in lista_objeto:
        mono.defender()

personajes2 = [Harry_potter,Legolas,Jack]
personaje_defender(personajes2)
