import os
import shutil
import send2trash  #  importado para enviar elementos eliminados a la papelera

archivo = open('curso.txt', 'w') # abrir pero con con el modulo os
archivo.write("texto de prueba")
archivo.close()

for i in os.listdir():
	print(i)

#  Es bastante util para hacer busqueda recursiva en directorios
ruta = "/home/lissandro/Escritorio/calculator-app-main"

for carpeta, subcarpeta, archivo in os.walk(ruta):
	print(f'en la carpeta {carpeta}')
	print(f'Las subcarpetas son:')
	for sub in subcarpeta:
		print(f'\t{sub}')
	print("Los archivos son")
	for arch in archivo:
		if arch.startswith('2015'):
			print(f'\t{arch}')
	print("\n")
# Mover elementos
#  shutil.move('curso.txt', '/home/lissandro/Escritorio/')


# Eliminar elementos
#  os.unlink('') Elimina el archivo del directorio indicado
#  os.rmdir() Elimina un dirfectorio vacio
#  elimina absolutamente el arbol, no recomendable
#  shutil.rmtree()


# modulo para enviar a la papelera el archivo (se tiene que instalar)
send2trash.send2trash('curso.txt')
