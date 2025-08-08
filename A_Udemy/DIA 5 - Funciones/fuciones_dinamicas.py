def chequear_3_cifras(lista):
    numero_tres_c = []

    for n in lista:
        if n in range(100, 1000):
            numero_tres_c.append(n)

        else:
            pass

    return numero_tres_c


resultado = chequear_3_cifras([555, 99, 6000, 443, 33, 111])
print(resultado)


def suma(a, b):
    resultado = a + b
    return resultado


print(suma(6, 6))


def celcius_a_farenheit(celcius):
    farenheit = (celcius * 9 / 5) + 32
    return farenheit


print(celcius_a_farenheit(45))


#--------------------------------


def vocales_texto(texto):
    vocales = ["a", "e", "i", "o", "u"]
    total = 0
    for v in vocales:
        total += texto.count(v)
    else:
        pass
    return total


texto = 'aeiou'.lower()
print(vocales_texto(texto))


def cuadrado(n):
    numero = n ** 0.5
    return round(numero, 3)


n = 150
print(cuadrado(n))


def es_primo(n):
    if n < 2:  # Ningún número menor que 2 es primo
        return False
    if n == 2 or n == 3:  # 2 y 3 son números primos
        return True
    if n % 2 == 0 or n % 3 == 0:  # Si es divisible por 2 o 3, no es primo
        return False

    # Verificar otros divisores desde 5 en adelante
    i = 5
    while i * i <= n:  # Solo necesitamos comprobar hasta la raíz cuadrada de n
        if n % i == 0 or n % (i + 2) == 0:  # Verifica si es divisible por i o i+2
            return False
        i += 6
    return True  # Si no se encontró ningún divisor, entonces es primo


print(es_primo(90))


def sumar(a, b):
    suma = a + b
    return suma


print(suma(6, 6))


def saludar(nombre):
    print("hola " + nombre)


saludar("luis")


def longitud_cadena(cadena):
    print(len(cadena))


longitud_cadena("Luisito, necesito ayuda")


def es_par(n):
    if n % 2 == 0:
        return True  # Devuelve True si el número es par
    else:
        return False  # Devuelve False si el número es impar


n = 1
print(es_par(n))  # Esto imprimirá False, ya que 1 no es par


def multiplicar(a, b):
    resul = a * b
    return resul


print(multiplicar(4, 5))


def es_negativo(n):
    if n < 0:
        return True
    else:
        return False


print(es_negativo(-5))


def centimetros_a_metros(metros):
    centimetro = metros * 100 / 1
    return centimetro


print(centimetros_a_metros(5))


def mayor_de_dos(a, b):
    if a > b:
        return True
    elif b > a:
        return False


print(mayor_de_dos(31, 5))


def cuadrado(n):
    return n * n


def sumar_cuadrados(a, b):
    return cuadrado(a) + cuadrado(b)


# Usando las funciones
resultado = sumar_cuadrados(3, 4)
print(resultado)  # Esto imprimirá 25, ya que 3^2 + 4^2 = 9 + 16 = 25


def cantidad_pares(lista_numeros):
    numeros_pares = 0
    for n in lista_numeros:
        if n % 2 == 0:
            numeros_pares += 1

    return numeros_pares


lista_numeros = [2,3,3,3,3,3,3,3,3,3,3,3,3,33,4,6,8,10,12]
print(cantidad_pares(lista_numeros))
