class Pajaro:
   alas = True # todos los objetos tienen este valor
   def __init__(self, color,  especie): #Contructor de la clase
    self.color = color
    self.especie = especie
   
   def piar(self): # Argumento posicional
    print('pio')

   def volar(self, metros):
    print(f"El pajaro ha volado {metros} metros")
    self.piar()

   def pintar_negro(self):
        self.color = "negro"
        print(f" Ahora el pajaro es {self.color}")

    #Metodos de clase
   @classmethod # Decorador metodo de clase no necesita instancia, pero no puede acceder a sus atributos.
   def poner_huevos(cls, cantidad): # solo al cls, que es la clase misma en si.
    print(f"Puso {cantidad} de huevos")
    cls.alas = False
    print(Pajaro.alas)

   @staticmethod # No puede acceder a ningun atributo
   def mirar():
     print("El pajaro mira")
      

Pajaro.mirar()
#Mas Ejemplos

class Mascota:
    def __init__(self):
        ...
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
        
Mascota.respirar()
        
#Ejemplo de como modifica el atributo de clase, el metodo class
class Jugador:
    vivo = False
    def __init__(self):
        ...
    @classmethod
    def revivir(cls):
        cls.vivo = True
        

luis = Jugador()
luis.revivir
