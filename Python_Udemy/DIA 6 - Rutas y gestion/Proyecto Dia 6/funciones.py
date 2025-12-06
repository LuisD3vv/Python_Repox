from pathlib import Path
import sqlite3
import os 
from time import sleep


db = 'Recetas.db'
ruta = os.path.join(os.path.dirname(__file__),db)



def validar_plataforma():
	"""
	funcion para formatear el sistema de comandos de la funcion system
	para que funcione en windows o linux repectivamente
	"""
	sistema = []
	if os.name == "posix":
		print("Sistema Linux")
		sistema.append("clear")
	else:
		print("Sistema Windows")
		sistema.append("cls")
	return "".join(sistema)


def crear_Receta():
	os.system(validar_plataforma())
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("SELECT Categoria FROM Categoria")
		titulos = cur.fetchall()
		if not titulos:
			print("No hay categorias disponibles")
			return
		print("Aqui tienes las categorias que tal ves te sirvan de inspiracion:")
		for Categoria in titulos:
			print("•",*Categoria)


	print("Crear receta")
	print("Ingresa el nombre de la receta.")
	nombre = input(">> ")
	print("ingresa la categoria de la receta: ")
	categoria = input(">> ")
	print("Ingresa el contenido de la receta.")
	print("Ingresa FIN para salir")
	contenido = []
	while True:
		texto = input(">> ")
		if texto.upper() == "FIN":
			break
		contenido.append(texto)
	final = "\n".join(contenido)
	try:
		with sqlite3.connect(ruta) as con:
			cur = con.cursor()
			cur.execute('CREATE TABLE IF NOT EXISTS Recetas ('
						'Receta_ID INTEGER PRIMARY KEY AUTOINCREMENT,'
						'Titulo TEXT NOT NULL,'
						'Contenido TEXT NOT NULL,'
						'Categoria TEXT NOT NULL'
						')')
			con.commit()
			cur.execute("INSERT INTO Recetas(Titulo,Contenido,Categoria) VALUES (?,?,?)", (nombre, final, categoria))
			con.commit()
			os.system(validar_plataforma())
			print("Receta creada exitosamente")
	except sqlite3.OperationalError as e:
		print("Ha ocurrido un error")
		log = open("Logs/error.log", "a")
		log.write(f"Ha ocurrido un error {e}\n")
		log.close()



def leer_receta():
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("SELECT Titulo FROM Recetas")
		titulos = cur.fetchall()
		os.system(validar_plataforma())
		print("Recetas disponibles:")
		for receta in titulos:
			print("•",*receta)
	print("¿Cual receta te gustaria leer?")
	eleccionreceta = input(">> ")
	if eleccionreceta.lower() == "ninguna":
		print("Regresando al menu")
		return
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("SELECT Contenido FROM Recetas WHERE titulo LIKE ?", (eleccionreceta,))
		cate = cur.fetchone()
		if not cate:
			os.system(validar_plataforma())
			print("No se encontro ninguna coincidencia.")
		else:
			cate = cate[0]
			print(f"DEBUG #1 {type(cate)} {cate}")
			os.system(validar_plataforma())
			print("-"*50)
			print("Receta:")
			print(*cate)
			print("-"*50)




def crear_categoria():
	print("crear categoria")
	nombreCategoria = input("Ingresa el nombre de la categoria: ")
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("INSERT INTO Categoria(Categoria) VALUES (?)", (nombreCategoria,))
		conn.commit()
		os.system(validar_plataforma())
		print("categoria creada exitosamente")



def eliminar_Receta():
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("SELECT Titulo FROM Recetas")
		titulos = cur.fetchall()
		print("Recetas disponibles:")
		for receta in titulos:
			print("•",*receta)
    
    
	NombreRecetaEliminar = input("Ingresa el nombre de la receta a eliminar: ")
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("DELETE FROM Recetas WHERE Titulo LIKE (?)", (NombreRecetaEliminar,))
		conn.commit()
		print(f"receta {NombreRecetaEliminar} eliminada exitosamente")



def eliminar_categoria():
	#  verificar si hay categoria
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("SELECT Categoria FROM Categoria")
		titulos = cur.fetchall()
		if not titulos:
			print("No hay categorias disponibles")
			return
		print("Categorias disponibles:")
		for Categoria in titulos:
			print("•",*Categoria)

	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("SELECT * FROM Categoria")
		hay = cur.fetchone()
		if hay != " ":
			NombreCategoriaEliminar = input("Ingresa el nombre de la categoria a eliminar: ")
			print("Al eliminar la categoria, todas las recetas dentro seran eliminadas")
			print("estas seguro?")
			seguir = input(">> ")
			if seguir.lower() == "si":
					cur.execute("delete from Categoria where Categoria like (?)", (NombreCategoriaEliminar,))
					conn.commit()
					print(f"Categoria {NombreCategoriaEliminar} eliminada exitosamente.")
			else:
				os.system(validar_plataforma())
				print("Volviendo al menu.")
				return
		else:
			print("No hay ninguna categoria")



def modificar_receta():
	os.system(validar_plataforma())
	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("select Titulo from Recetas")
		titulos = cur.fetchall()
		print("Recetas disponibles:")
		for receta in titulos:
			print("•",*receta)

	print("¿Cual receta te gustaria editar?")
	eleccionreceta = input(">> ")
	print("Ingresa el nuevo contenido de la receta:")
	print("Ingresa FIN para salir")
	contenido = []
	while True:
		texto = input(">> ")
		if texto.upper() == "FIN":
			break
		contenido.append(texto)
	final = "\n".join(contenido)


	with sqlite3.connect(ruta) as conn:
		cur = conn.cursor()
		cur.execute("UPDATE Recetas SET Contenido = ? WHERE titulo LIKE ?", (final,eleccionreceta))
		conn.commit()
		os.system(validar_plataforma())
		print("Se ha actualizado la receta",eleccionreceta)


def limpiar():
	print("Limpiando...")
	sleep(2)
	print("Listo!!")
	os.system(validar_plataforma())