"""
Lissandro 9/01/2025
"""
def contar_primos(numero): # Creamos la funcion con el parametro de numero

    primos = [2] # Definimos la lista donde se guardaran los primos, por conveniencia ponemos dos para que emepice esde ahi
    iteracion = 3

    if numero < 2:
        return 0
    while iteracion <= numero:

         for n in range(3,iteracion,2):

            if iteracion % n ==  0:
                iteracion += 2
                break
         else:
             primos.append(iteracion)
             iteracion += 2

    print(primos)
    return len(primos)


print(contar_primos(15))