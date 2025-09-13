"""
Lissandro AG 06/01/2025
"""
def devolver_distintos(a, b, c):
    suma = a+b+c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


print(devolver_distintos(10,13,11)) #recomendado cuando hay return, ya que este devuleve valores pero no lo imprime
