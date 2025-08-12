"""
El proyecto del dia de hoy es generar un turnero
es decir un programa que segun a que area nos dirigamos
nos de un turno con la inicial de esta area.
"""
import time
from numeros import *
from datetime import date

"""
Utilizar lfill para colocar 0 en numeros menores a 10

Sintaxis interesante

''.join((map(str, iterable)))
"""
fecha = date.today()
opcion = 0

# Prototipo
print("Cargando...")
time.sleep(2)
print("Bienvenido a Farmacias Python\nQue deseas realizar hoy")
"""
Las funciones no necesitan ser guardadas en una variable ni impresas, esto debido a que ya imprimen al ser llamadas
y solamenet esperan el argumento para ejecutarse
"""
def main():
	bucle = True
	while bucle:
		print("Selecciona una opcion")
		print("1) Farmacia\n2) Cosmetica\n3) Cita Medica\n4) Salir")

		try:
			opcion = input(">> ")
			if opcion not in ["1", "2", "3", "4"]:
				print("Opcion fuera del rango")
				continue
			match opcion:
				case "1":
					print("Generando turno...")
					decorador("F")
					time.sleep(2)
					print("Quires generar otro turno? [S] [N]")
					turno_farmacia = input(">> ")
					if turno_farmacia.lower() == "s":
						decorador("F")
					else:
						continue
				case "2":
					print("Generando turno...")
					decorador("C")
					time.sleep(2)
					print("Quires generar otro turno? [S] [N]")
					turno_cosmetica = input(">> ")
					if turno_cosmetica.lower() == "s":
						decorador("C")
					else:
						continue
				case "3":
					print("Generando turno...")
					decorador("M")
					time.sleep(2)
					print("Quires generar otro turno? [S] [N]")
					turno_Cita = input(">> ")
					if turno_Cita.lower() == "s":
						decorador("M")
					else:
						continue
				case "4":
					print("Has salido.")
					print(f"utimo acceso {fecha}")
					bucle = False
				case _:
					print("opcion incorrecta")
					continue

		except ValueError as e:
			print(f"Ha ocurrido un error {e}")


main()
