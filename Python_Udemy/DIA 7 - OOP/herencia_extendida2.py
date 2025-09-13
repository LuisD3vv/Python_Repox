class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print('ja ja')
    def hablar(self):
        print("Que tal")

class Hijo(Padre, Madre): # Herencia multiple
    ...

class Nieto(Hijo):
    ...


mi_nieto = Nieto()

mi_nieto.hablar()
print(Nieto.__mro__) # imprimir orden de herencia / method resolution order


