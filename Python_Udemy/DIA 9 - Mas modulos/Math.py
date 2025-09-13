import math
from math import  nan as NaN

n = 9.9
resultado_piso = math.floor(n)
resultado_techo = math.ceil(n)
#  este es menos impresiso que el que ya tiene
#  incluida la base

"""
resultado1 = math.log(25,10)
resultado2= math.log10(25)

output 1 | 1.3979400086720375
output 2 | 1.3979400086720377

"""
logaritmo_con_opcion = math.log(100, 5)
pi = math.pi
exponente = math.exp(2)
factorial = math.factorial(3)
logaritmobase2 = math.log2(4)
euler = math.e
asoluto = math.fabs(4)

numero = "1"

if numero is NaN:
	print(numero)
else:
	print("no es un numero")

