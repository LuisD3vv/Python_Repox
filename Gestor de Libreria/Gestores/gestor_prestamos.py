from datetime import date
import sqlite3

hoy = date.today()

ruta_db = "/home/lissandro/Python_Repox/Gestor de Libreria/extra/GestorGeneral.db"

def validadar_metodo(*args):
	# Si esperas que el argumento sea 1, args llega como tupla, por eso se compara con args[0]
	if args[0] == 1:
		table_id = args[1]
		try:
			with sqlite3.connect(ruta_db) as conn:
				cur = conn.cursor()
				cur.execute("SELECT nombre, apellido FROM Usuario WHERE User_id = ?", (table_id,))
				user_actual = cur.fetchone()  # traer un solo resultado
				if user_actual:
					return "id existente"
				else:
					print("Culo")
		except sqlite3.Error as error:
			print('Hubo un error =>', error)
	elif args[0] == 2:
		nom = args[1]
		ape = args[2]
		try:
			with sqlite3.connect(ruta_db) as conn:
				cur = conn.cursor()
				# Para poder trabajar con algunos caracteres como los %% de sql, es necesario formatear el string con cadenas literales
				cur.execute("SELECT User_id, Nombre FROM Usuario WHERE (Nombre like ?) and (Apellido like ?)", (f"%{nom}%", f"%{ape}%"))
				user_actual = cur.fetchone()  # traer un solo resultado
				if user_actual:
					return "usuario existente"
				else:
					print("Culo")
		except sqlite3.Error as error:
			print('Hubo un error =>', error)
	return None


def prestar_libro(*args):
	"""Funcion que verifica el estado del libro
	si esta prestado o no, y asi, podemos cambiar
	el estado del libro segun se de el caso"""


def devolver_libro():
	"""Funcion que devuelve el estado del libro"""


def ver_prestamos():
	"""Funcion que devuelve el estado de los
	libros, si estan disponibles para ser
	prestados o aun hay que esperar"""



