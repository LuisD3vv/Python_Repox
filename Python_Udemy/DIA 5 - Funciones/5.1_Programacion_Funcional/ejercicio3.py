from functools import reduce
import os


# List of songs with their durations (in minutes)
playlist = [
    ('What Was I Made For?', 3.42),
    ('Just Like That', 5.05),
    ('Song 3', 6.55),
    ('Leave The Door Open', 4.02), 
    ('I Can\'t Breath', 4.47), 
    ('Bad Guy', 3.14)
    ]


# Repasar el pinche map, filter y el reduce , estas funciones ya iteran sobre los elementos
# por eso solo tenemos que aplicar una funcion.
os.system("clear")
def duracion(lista):
    return lista[1] > 5.00

print("Canciones de mayor duracion")
max_duracion = filter(duracion,playlist)
print(list(max_duracion))

def minutesToSeconds(lista):
    return lista[1] * 60

print("Minutos a segundos")
totalSeconds = list(map(minutesToSeconds,playlist))
print(totalSeconds)

# el reduce necesita dos elementos, el acomulador y el elemento
def totalPlaytime(a,lista):
    numero = lista[1]
    return a + numero

print("La duraciones total de la playlist es de:")
totaltime = reduce(totalPlaytime,playlist,0)
print(f"{totaltime} minutos")
'''
se multiplica porque estas pasando una unidad mas pequenna, en mas grande en numero
de lo contrario, si quisieramos los minutos, deberiamos de dividir para obtener numeros mas grandes y significativos

1 minuto = 60 segundos (minutos*60)
60 segundos = 1 minuto (minutos/60)
'''
