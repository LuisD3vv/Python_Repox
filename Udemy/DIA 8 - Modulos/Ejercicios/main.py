from Calculadora import suma as sum,resta as res,division as div,multiplicacion as mult
try:

	while True:
		print("Ingresa la opcion")
		print("1.-Suma\n2.-Resta\n3.-Division\n4.-Multiplicacion\n5.-Salir\n")
		operacion = int(input(">> "))
		if operacion == 1:
			print("Suma: ")
			a = int(input("a >> "))
			b = int(input("b >> "))
			print(f"Resultado: {sum(a, b)}")
			continue

		elif operacion == 2:
			print("Resta: ")
			a = int(input("a >> "))
			b = int(input("b >> "))
			print(f"Resultado: {res(a, b)}")
			continue

		elif operacion == 3:
			print("Multiplicacion: ")
			a = int(input("a >> "))
			b = int(input("b >> "))
			print(f"Resultado: {mult(a, b)}")
			continue

		elif operacion == 4:
			print("Division: ")
			a = int(input("a >> "))
			b = int(input("b >> "))
			print(f"Resultado: {div(a, b)}")
			continue
		elif operacion == 5:
			print("Has salido")
			break
except KeyboardInterrupt:
	print("Has salido por interrumpcion")
