class Vehiculo:
	def __init__(self,marca,color):
		self.marca = marca
		self.color = color

class Coche(Vehiculo):
	def __init__(self,marca,color,potencia,motor):
		# Asi llamamos al constructor padre desde la clase hija.
		super().__init__(marca,color)
		self.potencia = potencia
		self.motor = motor
	def __str__(self):
		return f"Modelo {self.marca} | Potencia {self.potencia} | Color {self.color} | Motor {self.motor}"


auto = Coche(marca="Chevrolet",color="Rojo",potencia="700HP",motor="V8")
try:
	if isinstance(auto,Coche):
		print("Si es un objeto")
	else:
		print("culo")
except ValueError:
	print("Error")
finally:
	print(auto)