"""
En Python, la palabra clave yield
se utiliza para definir funciones
generadoras. Estas funciones,
a diferencia de las funciones 
normales que retornan un valor único,
pueden pausar su ejecución
y reanudarla posteriormente, 
devolviendo valores de forma gradual.

asi pudiendo ejecutar funciones que devuelvan un valor 
cuando se requiera que este aumente pero no al instante
como un turnero
"""
# es muy util para hacer iteraciones donde se requiere que el valor generado no se de todo de repente

def mi_funcion():
    lista= []
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x * 10

# yiel significa producir, un generador

print(mi_generador())
print(mi_funcion())


g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def mi_generador2():
    x = 1
    yield x 
    
    x += 1
    yield x

    x += 1
    yield x


j = mi_generador2()
print(next(j))
print(next(j))
print("Hola mundo")
print(next(j))


# Ejemplo de como usarlo para gener un loop infinito

def secuencia_infinita():
    """
    Como no hay 
    alguna conficion que lo detenga
    cada que se llame se seguira aumentando el 
    valor
    """
    num = 0
    while True:
        yield num
        num += 1

generador = secuencia_infinita()

print(next(generador))


def multiplos():
    num = 7
    for x in range(1,11):
       yield x * num

generador = multiplos()

for x in range(1,11):
    print(next(generador))


def quitar_vidas():
    vidas = 3
    while vidas > 0:
        print(f"Tienes {vidas} vidas")
        yield vidas
        vidas -= 1
    print("¡Game over!")


perder_vidas  = quitar_vidas()
print(next(perder_vidas))
print(next(perder_vidas))
print(next(perder_vidas))

# Yo pensando en una solucion logica y me salen con esta mamada

def quitar_vidas():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
    
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x

perder_vida = quitar_vidas()
