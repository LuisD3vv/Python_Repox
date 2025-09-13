import random, time

dice = [1, 2, 3, 4, 5, 6]

# K es el número de resultados de esa lista
#  print(random.choices(dice, k=3))

def slot(result):
	"""Una manera elegante de contar resultados."""
	if result.count('7') == 3:
		return "jackpot"
	else:
		return "Gracias por jugar"

# Los Prints van antes de time.sleep...


intentos = 0
print("Loading...")
time.sleep(3)
print("Ready!")
while True:
	try:
		symbols = ['🍒', ' 🍇', '🍉', '7']
		#  prueba = ['7','7','7']
		result = random.choices(symbols, k=3)
		print(*result, sep=" | ")
		if slot(result) == "jackpot":
			print("Jackpot!!")
			print(f"Lo has logrado en {intentos} intentos.")
			break
		else:
			seguir = input("Seguir tirando: (Y-N): ").lower()
			if seguir == "y":
				intentos += 1
				continue
			elif seguir == "n":
				break
	except TypeError:
		print("Ingresa correctamente la opcion.")
	except IndexError:
		print("Hay un error en el indice")
	except ValueError:
		print("El valor debe ser un string")
	else:
		continue





