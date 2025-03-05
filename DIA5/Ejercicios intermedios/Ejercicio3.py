"""
Lissandro 11/01/2025
"""
# Codigo que devuelva valores booleanos dado el caso que haya mas de un cero consecutivamente
"""
    lista = {1,3,4,54,3,4,0,0} #output True
"""


def ceros(*args):  # la razon del -1 es para evitar que el indice que coloquemos se salga del rango.
    contador = 0
    for num in range(len(args) - 1):  # Utilzamos el largo de args como un rango de busqueda que se base en el mismo largo de args.
         if args[num] == 0 and args[num + 1] == 0:
            return True  # En cuanto encuetra la coincidencia, se detiene
         else:
             contador += 1

    return False


print(ceros( 0,2,0, 3, 0,1, 0, 23, 4))

# indices ce(0, 1, 2, 3,  4,  5,  6, 7, )
