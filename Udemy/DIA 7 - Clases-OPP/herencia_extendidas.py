class Animal:
    """Self es una conveniencia, tanto 
    como lo es args, cls y kwars
    """
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacen(self):
        print("Este animal ha nacido")
    
    def hablar(self):
        print("Este animal emite sonido")


class Pajaro(Animal): # Se le pasa como parametro el nombre de la clase para heredar
    def __init__(self, edad, color,altura_vuelo):
        #Super nos permite reutilizar metodos isn reencirbilos desde la subclase
        super().__init__(edad,color) # Evitar repetir datos heredados con self()
        self.altura_vuelo = altura_vuelo #este es el atributo propio de esta clase
    
    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


Piolin = Pajaro(2,"Amarillo",60)
Mi_animal = Animal(5,"negro")
Piolin.volar(12)

