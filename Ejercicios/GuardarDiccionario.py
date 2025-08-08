from pathlib import Path

ruta = Path("LineaPorLinea.txt")

Nombre_edad = {"Lissandro": 22, "Eduardo": 24, "William": 20}

try:
	with open(ruta, "a") as file:
		for clave, valor in Nombre_edad.items():
			file.writelines(f"{clave}: {valor}\n")
except FileNotFoundError:
	print("No existe el archivo")
finally:
	print("FIN")
