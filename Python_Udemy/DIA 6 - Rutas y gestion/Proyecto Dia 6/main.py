import os
import sqlite3
from os import *
import shutil  # poder eliminar y realizar operaciones de alto nivel
import time
from pathlib import Path  # Manipular y crear rutas
from funciones import *

db = 'Recetas.db'
ruta = os.path.join(os.path.dirname(__file__),db)

def validar_plataforma():
	if os.name == "posix":
		return "clear"
	else:
		return "cls"


def numerorecetas():
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("Select count(Receta_ID) from Recetas")
		total = cur.fetchone()
		todo = total[0]
		return todo

def main():
	system(validar_plataforma())
	# print(type(total))
	while True:
		print(f"Recetas disponibles: [ {numerorecetas()} ]")
		print(f"========================")
		print(f"Bienvenido a Recetame!")
		print("•1) Leer Receta\n"
			"•2) Crear Receta\n"
			"•3) Crear Categoria\n"
			"•4) Eliminar Receta\n"
			"•5) Eliminar Categoria\n"
			"•6) Modificar Receta\n"
			"•7) Limpiar Consola\n"
			"•8) Salir\n")
		print("\u00A9 2025 LuisD3v")
		print(f"========================")
		print('¿Que deseas realizar?')
		opcion = input(">> ")	
		try:
			opcion = opcion.lower()
		except ValueError:
			system(validar_plataforma())
			print("< Es necesario que ingreses un numero >")
		except KeyboardInterrupt:
			print("Saliendo...")
		else:
			match opcion: # type: ignore
				case "1" | "leer receta":
					leer_receta()
				case "2" | "crear receta":
					crear_Receta()
				case "3" | "crear categoria":
					crear_categoria()
				case "4" | "eliminar receta":
					eliminar_Receta()
				case "5" | "eliminar categoria":
					eliminar_categoria()
				case "6" | "modificar receta":
					modificar_receta()
				case "7" | "limpiar consola":
					limpiar()
				case "8" | "salir":
					system(validar_plataforma())
					print("Has salido exitosamente.")
					exit()  # Salida logica del codigo
main()
