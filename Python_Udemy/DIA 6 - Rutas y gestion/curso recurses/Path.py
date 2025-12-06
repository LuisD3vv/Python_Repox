from pathlib import Path
print("\n")
# Constructor path es la base de todo el sistema de archivos
base = Path.home() # /home/usuario/
print(base)
# Generar una ruta absoluta
guia = Path(base,"Europa","Mexico", Path("Barcelona", "Culiacan.txt"))
print(guia)
guia2 = Path(base,"Europa", "Mexico")
print(guia2)
guia3 = guia.with_name("la_Pedrera.txt")
print(base, guia3)
print(guia.parent)
print(guia.parent.parent) # va subiendo el nivel hacia arriba


# parent devuelve el antecesor de la ruta, es como un cd ../../ en linux
# Con esto podemos generar rutas con trozos de otras rutas

# Ejemplo con directorios usando glob
guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("**/*txt"): # Busca de manera recurivisa
    print(txt)
"""
Los dos asteriscos y la barra invertida nos quiere decir que
buscara en carpetas y subcarpetas
"""

# Ejemplo para recuperar un pedazo de ruta

guia = Path("Europa", "España", "sagrada_familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)