from pathlib import Path
import os
# Ruta relativa


ruta = Path("A_Udemy/DIA 6 - Rutas y gestion archivos/Directorio de pruebas/nombres.txt")
"""
un error es tratar de utilizar las rutas de windows en linux, por eso no detectaba mi archivo

en el otro caso seria 

ruta = Path("A_Udemy\\DIA 6 - Rutas y gestion archivos\\Directorio de pruebas\\nombres.txt")

las dobles barras son para escapar su significado literal
"""

lectura = open(ruta, "r")

#devuelve una lista
print(lectura.readlines())

# lee el archivo completo
print(lectura.read())
# le una linea
print(lectura.readline())

# # cerramos el archivo 
lectura.close()

# o manejo de contexto with as
with open (ruta) as lectura:
    print(lectura.read())

directorio_actual = os.getcwd()

directorio_nombre = os.path.join(directorio_actual)
print(directorio_nombre)
print(directorio_actual)

print(os.path.isfile(directorio_nombre))


# manejando execpciones


try:
    with open (ruta) as lectura:
        #  seek mueve el cursor a una localizacion deseada en el archivo
        print(lectura.seek(10))
        # nos permite eliminar o remover contenido desde cierto punto pasado como parametro, es decir lee hasta cierto punto
        print(lectura.truncate(10))
finally:
    print("exito")