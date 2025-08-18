import time

from time import *
import timeit

"""
	nos ayuda a conocer el timepo de ejecucion de un codigo

 Timeit requiere de dos parametros, declaracion y la funcion, junto con el argunmento de 
 number que es cuantas veces quieres repetir el experimento
 La sintaxis es esta
 
 timeit.timeit(declaracion,setup,number=repeticiones)
 
 
 """
time.sleep(3)

declaracion = '''
prueba_for(10)
'''
mi_setup = '''
def prueba_for(numero):
	lista = []
	for num in range(1, numero + 1):
		lista.append(num)
	return lista
'''
duracion = timeit.timeit(declaracion, mi_setup, number=10000000)
print(duracion)


declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
	lista = []
	contador = 1
	while contador <= numero:
		lista.append(contador)
		contador += 1
	return lista
'''

duracion2 = timeit.timeit(declaracion2, mi_setup2, number=10000000)
print(duracion2)

"""
Tambien tenemos la otra forma con time

incio = time.time()
funcion(argumento)
final = time,.time()
duracion = (final-inicio

"""


