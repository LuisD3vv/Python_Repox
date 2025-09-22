# Ejercicio 1 ----------------
class Persona:
    """Clase persona"""
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola {self.nombre} tu edad es {self.edad}")


Luis = Persona("Luis",21)
Luis.saludar()

# Ejercicio 2 ----------------

class Circulo:
    """
    Clase para calcular area y perimetro 
    segun el radio otorgado por el usuario
    """
    def __init__(self,radio):
        self.radio = radio
    def calcular_area(self):
        """Calcular area"""
        area = 3.1416 * pow(self.radio,2)
        print(f"El area es {round(area,2)}")
    def calcular_perimetro(self):
        """Calcular perimetro"""
        perimetro = (2 * 3.1416) * self.radio
        print(f"El perimetro es {round(perimetro,2)}")
    def __str__(self):
        return "Los valores estan redondeados a dos digitos"

medidas  = Circulo(10)
medidas.calcular_area()
medidas.calcular_perimetro()


# Ejercicio 3 ----------------

class Animal:
    """Clase animal"""
    vertebrado = True
    """Clase generica perro"""
    def hacer_sonido(self):
        print("Sonido Generico")

#Ejemplo de polimorfismo
class Perro(Animal):
    """Clase perro hereda atributos de animal"""
    def hacer_sonido(self):
        print("Guau!")


Animal1 = Animal()
Animal1.hacer_sonido()

Scooby = Perro()
Scooby.hacer_sonido()
print("El perro es vertebrado?",Scooby.vertebrado)


# Ejercicio 4 ----------------

class CuentaBancaria:
    """Cuenta bancaria de ejercicio"""
    interes_anual = 25.75
    def __init__(self,capital_inicial):
        self.capital_inicial = capital_inicial
    def calculo(self):
        """
        Realizar calculo
        """
        nuevo = self.capital_inicial  * (CuentaBancaria.interes_anual / 100) * 1
        return f"Cantidad inicial ${self.capital_inicial}, con una tasa del {CuentaBancaria.interes_anual}% Anual = ${self.capital_inicial + nuevo}"
    def __str__(self):
        return f"Interes actual {CuentaBancaria.interes_anual}%"
    @classmethod
    def cambiar_interes(cls,nuevo_interes):
        """
        Cambio de interes
        """
        if nuevo_interes == 0:
            # Si el usuario desea mantener la tasa ya proporcionada
            cls.interes_anual = cls.interes_anual
        else:
            cls.interes_anual = nuevo_interes
    @staticmethod
    def imprimir_cantidad(cantidad):
        """
        Impresion nomas porque si
        """
    # Realizar la operacion y la impresion
        return "Cualquier duda llamar al 6673273581"

# Creo el objeto
calcular = CuentaBancaria(1500)
# Cambio el interes
calcular.cambiar_interes(0)
print(calcular.calculo())
# doy una cantidad
print(calcular)


# Ejercicio 5 ----------------

class Producto:
    """
    Crear clase
    """
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    
    #Getter
    @property
    def precio(self):
        """
        Creamos un getter para obtener y regresar
        un atributo como si fuera privado
        """
        #print("Getter activado")
        return self._precio # colocarlo con punto causa recursion infinita
    
    
    #Setter / Controla la validacion, dependiendo de la condicion puede o no crearse el objeto
    @precio.setter
    def precio(self, precio_nuevo):
        #print("Setter activado")
        # El setter valida o procesa antes de asignar
        if precio_nuevo < 0:
            print("Porfavor, ingresa un numero positivo")
            self._precio = None
        else:
            self._precio = precio_nuevo # Aqui se define el setter, el nuevo nombre de precio mas protegido
            
    def conocer_precio(self):
        """
        Impresion del valor
        """
        print(f"Producto: {self.nombre} - Precio: {self.precio}")
        
        
prod1 = Producto("Coca Cola", 30)
prod2 = Producto("Pepsi", 21)
prod3 = Producto("Vive cien", 17)
prod4 = Producto("Prime", 20)
prod5 = Producto("Volt", 23)
prod6 = Producto("Amper", 20)

products = [prod1,prod2,prod3,prod4,prod5,prod6]

for elemento in products:
    elemento.conocer_precio()

# Ejercicio 5 -------- ejemplo sin getter ni setter

class Temperatura:
    def __init__(self,grados):
        self.grados = grados
        
        
t = Temperatura(-500)
print(t.grados)

# Con encapsulamiento

class Temperatura2:
    def __init__(self, grados):
        self.grados = grados  # usa el setter

    @property
    def grados(self):
        # Solor nos sirve para leer
        return self._grados  # getter devuelve el valor real / en la memoria

    @grados.setter
    #  Aqui si podemos modificar el dato
    def grados(self, nuevo_valor):
        if nuevo_valor < -273.15:
            print("❌ Temperatura por debajo del cero absoluto no permitida.")
        else:
            self._grados = nuevo_valor


ts = Temperatura2(-500)
ts.grados = 25
print(ts.grados)


# Ejercicio 6 -------- ejemplo con getter

class usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 13:
            print("Edad no permitida para crear esta cuenta")
        else:
            print("Edad aceptada")
            self._edad = nueva_edad


luis = usuario("Luis", 10)
luis.edad = 21
print(luis.edad)
luis.edad = 10 # Como el valor es invalido lo rechaza, por eso  sigue conservando el valor que cumplio la condicion 25
print(luis.edad)
luis.edad = 30
print(luis.edad)

"""
Estos metodos nos ayudan a que no se guarden datos
inconsistentes o en un estado invalido, permitiendo
de esta forma solo guardar los que cumplan con la
condicion indicada en el setter.
"""

class Equipo:
    def __init__(self,lista):
        self.Jugadores = {}
        # {'Luis':'Portero'}
        
        for nombre in lista:
            self.Jugadores[nombre] = None
            
    def agregar_jugadores(self, nombre,posicion):
        self.Jugadores[nombre] = posicion
        
    def mostrar_posicion(self):
        for nombre, posicion in self.Jugadores.items():
            print(f"Actuales: {nombre}: {posicion}")      
            
    def eliminar_jugador(self,nombre):
        """metodo para eliminar jugadores"""
        if nombre in self.Jugadores:
            jugador_eliminado = self.Jugadores[nombre]
            del self.Jugadores[nombre]
            print(f"Jugador eliminado [-{nombre}-] posicion [-{jugador_eliminado}-]")

Equipo1 = Equipo(['Luis','Eduardo','William'])
Equipo1.agregar_jugadores('Luis','Portero')
Equipo1.agregar_jugadores('Eduardo', 'Delantero')
Equipo1.agregar_jugadores('William','Defensa')

Equipo2 = Equipo(['Jose', 'Pablo', 'Yavhe'])
Equipo1.agregar_jugadores('Jose','Arbitro')
Equipo1.agregar_jugadores('Pablo', 'Delantero')
Equipo1.agregar_jugadores('Yavhe','Defensa')

Equipo1.mostrar_posicion()
Equipo2.mostrar_posicion()

Equipo1.eliminar_jugador('Luis')
Equipo1.mostrar_posicion()

# Siempre que quieras manipular datos internos de un objeto
# usa los métodos a través de la instancia, no de la clase.
