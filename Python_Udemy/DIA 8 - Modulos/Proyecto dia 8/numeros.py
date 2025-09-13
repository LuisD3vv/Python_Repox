"""
Con el while true
nos ayuda a generar numero
infinitos o mas bien
poder generar los que queremos

"""
def turnoFarmacia():
	n = 1
	while True:
		yield n
		n += 1

def turnoCosmetica():
	n = 1
	while True:
		yield n
		n += 1

def turnoCita():
	n = 1
	while True:
		yield n
		n += 1

# Aqui van los decoradores

f = turnoFarmacia()
c = turnoCosmetica()
m = turnoCita()

def decorador(rubro):
	print("-" * 23)
	print("El turno es:")
	if rubro == "F":
		print(f"F-{next(f)}")
	elif rubro == "C":
		print(f"C-{next(c)}")
	elif rubro == "M":
		print(f"M-{next(m)}")
	else:
		print("Desarrollado por Lissandro Dev")
	print("Espere a ser atendido.")
	print("-" * 23)
