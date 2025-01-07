
def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total


print(suma(899, 343, 4545, 44332, 454, 2354, 788, 766, 7))


def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg ** 2
    return total


print(suma_cuadrados(5, 10, 20, 50))


def valor_absoluto(num):
    if num < 0:
        return -num  # Convierte a positivo
    else:
        return num  # Mantiene el valor como está


def suma_absolutos(*args):
    total = 0
    for num in args:
        total += valor_absoluto(num)  # Usa la función para obtener el valor absoluto
    return total


print(suma_absolutos(-6, 78, -4, 5, -89, -32))


def numeros_personas(nombre, *args):
    suma_numeros = sum(args)
    print(f"{nombre}, la suma de tus numeros es {suma_numeros}")


numeros_personas("Luis", 55, 6, 5, 4, 32, 12)


def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [100,200,300,400]
kwargs = {'x': 'uno', 'z': 'dos', 'y': 'tres'}

prueba(10, 39, *args, **kwargs)


def cantidad_atributos(**kwargs):
   return len(kwargs)


total = cantidad_atributos(A = 8, B= 5, C = 9)
print(f"La cantidad de atributos es: {total}")

def lista_atributos(**kwargs):
    kwargs = list(kwargs.values())
    return kwargs


print(lista_atributos(a= 5, g = 4, b=4))

def describir_persona(nombre, **kwargs):
       print(f"Características de {nombre}:")
# desempaquetar diccionario


kwargs = {'color_ojos': 'Cafe', 'color_pelo': 'Cafe oscuro'}
describir_persona("Luis", **kwargs)
