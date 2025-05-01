lista = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
letra = "Sabina"
si = [i for i in letra if i == "S"]
print(si)
print(lista)

# Nos da un mejor enfonque, en el caso del ejemplo de arriba no necesitamos el expresion, ya que la expresion se esta tomando de la varibale de arriba.
pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]

print(metros)

# [nueva_elemento for elemento in iterable if condición]

pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]


# {clave: valor for elemento in iterable if condición}
pares_cuadrados = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares_cuadrados)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
