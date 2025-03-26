from pathlib import Path
# Constructor path
base = Path.home()
print(base)
# Generar una ruta absoluta
guia = Path(base,"Europa","Mexico", Path("Barcelona", "Culiacan.txt"))
guia2 = guia.with_name("la_Pedrera.txt")
print(guia.parent)

# parent devuelve el antecesor de la ruta, es como un cd ../../ en linux

# Ejemplo con directorios usando glob

guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("**/*txt"):
    print(txt)


"""
Los dos asteriscos y la barra invertida nos quiere decir que
buscara en carpetas y subcarpetas
"""

# Ejemplo para recuperar un pedazo de ruta

guia = Path("Europa", "espania", "sagrada_familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "espania"))
print(en_europa)
print(en_espania)