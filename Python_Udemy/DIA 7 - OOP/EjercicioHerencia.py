class Vertebrado:
    vertebrado = True
class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")


# No necesitamos heredar vertebrado, porque ya se hereda de manera indirecta a traves de las demas clases hijas
class Ornitorrinco(Ave,Reptil, Pez, Mamifero):
    """
    Caso curisoso, como todos las demas clases ya heredan
    vertebrado, no es necesario colocarlo en los parametros
    dado a qeu esta heredado directamente junto con los
    metodos de los demas.
    """
    ...

prry = Ornitorrinco()

prry.poner_huevos()
print(prry.tiene_pico)
print(prry.vertebrado)
print(prry.venenoso)
prry.nadar()
prry.caminar()
prry.amamantar()

print(Ornitorrinco.__mro__) # method order resolution

""" 
Method Resolution Order nos ayuda a conocer la jerarquia de las herencias que tiene una clase
a la cual se le aplican atributos de otra, por defecto es de derecho a izquierda, siendo tal y como estan en los parametros
"""
