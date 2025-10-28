class Alumno:
	def __init__(self,nombre,calificacion):
		self.nombre = nombre
		self.calificacion = calificacion


	def informacion_Alumno(self):
		return f"Nombre {self.nombre}"

	def verificar_calificacion(self):
		if self.calificacion <= 5:
			return f"Estas reprobado con {self.calificacion} de calificacion."
		else:
			return f"Estas aprobado con {self.calificacion}  de calificacion."



Lissandro = Alumno("Luis",2)

print(Lissandro.verificar_calificacion())
print(Lissandro.informacion_Alumno())