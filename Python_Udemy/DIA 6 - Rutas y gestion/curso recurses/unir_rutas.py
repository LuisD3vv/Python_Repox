import os
from os import mkdir
from pathlib import Path

# Para poder unir rutas tenemos dos formas disponibles

# con pathlib

ruta1 = Path("mi_archivo.txt")
ruta2 = Path("../Directorio de pruebas/documentos")
# Directorio base del sistema operativo
rutaExtra = Path.home() / ruta1

rutaUnida = ruta2 / ruta1
rutaUnida2 = ruta2.joinpath(ruta1)

# con os

ruta3 = os.path.join(rutaUnida, "mi_archivo" )

# El pathLib crea objetos tipo patho ruta y os no

"""
Las rutas se pueden modificar, eliminar y unir
Los archivos se pueden crear vacios y unir al final de una ruta como tal, tamien se puede unir con una ruta ya existente
"""

archivo = "nombres.txt"
rutaConArchivo = ruta2 / archivo

#o también, se debe de unir como string, ya que al momento de crearlo es donde pasa a ser un objeto real

archivo = "nombres"
rutaConArchivoUnido = ruta2 / (archivo + ".txt")

# Me falta repasar los demás metodos de las rutas

# para anadir un archivo primero se debe de crear la carpeta
carpteta = Path("../Directorio de pruebas/documentos")
carpteta.mkdir(parents=True, exist_ok=True)
# si se atraviesa alguna carpeta y la necesita la crear para completar la ruta, y si existe no lanzara ningun error
