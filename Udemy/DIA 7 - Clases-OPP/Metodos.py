class Pajaro:
   alas = True # todos los objetos tienen este valor
   def __init__(self, color,  especie):# Contructor de la clase / tambien llamado metodo magico
    self.color = color
    self.especie = especie
   
   def piar(self):
    print('pio, mi color es {}'.format(self.color))

   def volar(self, metros):
    print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro("Amarillo", 'canario')

piolin.piar()
piolin.volar(50)

"""
cada ves quu dentro de la clase se construya un metodo que invoque a un atributo
necesitas relacionarlo con el objeto al que pertenece
"""

class Mago:
    def __init__(self):
        ...
    def lanzar_hechizo(self):
        print("¡Abracadabra!")


merlin = Mago()

merlin.lanzar_hechizo()


class Alarma:
    """
    Clase principal
    """
    def __init__ (self):
        ... #Dentro de la clase debemos de colocar a que instancia se le aplica, por eso se pasas el self
    def postergar(self, cantidad_minutos):
        """
        imprimir 
        """
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


mensaje = Alarma()
mensaje.postergar(10)


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas   = cantidad_flechas
    def lanzar_flecha(self,cantidad_flechas):
        """
        Reducir cantidad de flechas al ser llamado este metodo
        """
        cantidad_flechas -= 1
        
        
Mario_bros = Personaje(10)
Mario_bros.lanzar_flecha()