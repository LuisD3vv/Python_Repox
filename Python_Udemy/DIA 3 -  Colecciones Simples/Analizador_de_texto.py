from collections import defaultdict

leer = open('texto_proyecto_dia3.txt', 'r')
texto = leer.read().lower()

letras = []
letra1 = input("ingresa la primera letra: ").lower()
letras.append(letra1)
letra2 = input("ingresa la segunda letra: ").lower()
letras.append(letra2)
letra3 = input("ingresa la tercer letra: ").lower()
letras.append(letra3)

letra1 = texto.count(letra1)
letra2 = texto.count(letra2)
letra3 = texto.count(letra3)

texto_total = len(texto)
texto_reversa = texto[::-1]
texto_primeraletra = texto[0]
texto_ultimaletra = texto[-1]

cantidad_letras = letra1, letra2, letra3
print("\n")
print("CANTIDAD DE PALABRAS:")
print(f'La cantidad de palabras en tu texto es de {texto_total}')

# voltear un texto
print("\n")
print("TEXTO EN REVERSA")
print(f"'{texto_reversa}'")

# cantidad de veces que aparece tu letra
print("\n")
print("CANTIDAD DE PALABRAS")
print(f'La primera letra tiene un total de {letra1} apariciones en tu texto ')
print(f'La segunda letra tiene un total de {letra2} apariciones en tu texto ')
print(f'La tercera letra tiene un total de {letra3} apariciones en tu texto ')

# buscar la primera letra
print("\n")
print("Buscar la primera y ultima letra de tu texto")
print(f'La primera letra de tu texto es {texto_primeraletra} y la ultima {texto_ultimaletra}')

# palabra python
print("\n")
print('Buscar la palabra python')
palabra = 'python' in texto
dic = {True: "si", False: "no"}
print(f'La palabra "python" {dic[palabra]} se encuentra en tu texto')

print("\n")
leer.close()


#  Comprobar si hay vocales

def contar_vocales(cadena):
	vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
	for letra in cadena.lower():
		if letra in ('a', 'e', 'i', 'o', 'u'):
			vocales[letra] += 1
	return vocales

def contar_vocales2(cadena):
	# con el defaultdict no necesitamos declarar nada
	#  ya que de n existir se creara y se le coloca un numero
	#  entero de 0 si se intenta acceder
	vocales = defaultdict(int)
	for letra in cadena.lower():
		if letra in ('a', 'e', 'i', 'o', 'u'):
			vocales[letra] += 1
	return vocales


print("Cantidad de vocales en tu texto: ")
contar = contar_vocales(texto)
contar2 = contar_vocales2(texto)
print(contar)
print(contar2)
