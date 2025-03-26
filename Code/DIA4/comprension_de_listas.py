lista = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
letra = "Sabina"
si = [i for i in letra if i == "S"]
print(si)
print(lista)

# Nos da un mejor enfonque, en el caso del ejemplo de arriba no necesitamos el expresion, ya que la expresion se esta tomando de la varibale de arriba.
pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]

print(metros)
