import sqlite3


with sqlite3.connect('Recetas.db') as conn:
	cur = conn.cursor()
	cur.execute("SELECT * FROM Recetas")
	todo = cur.fetchall()
	for receta in todo:
		print(receta)


print("Categorias")
with sqlite3.connect('Recetas.db') as conn:
	cur = conn.cursor()
	cur.execute("SELECT * FROM Categoria")
	todo = cur.fetchall()
	for receta in todo:
		print(receta)