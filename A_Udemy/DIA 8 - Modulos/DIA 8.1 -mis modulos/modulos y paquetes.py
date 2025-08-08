"""
Para descargar modulos, basta con 
buscar en internet el modulo que deseamos y
leer la documentacion de como funciona
lo descargamos de la siguiente manera

en mi caso como estoy en ubunto, requiero
de usar atp, si estas en windows puedes
usar directamente pip install paquete

yo utilice este

sudo apt install python3-nombre-del-paquete
o pip install <Nombre del paquete>

Asi instalamos mediante apt, el modulo de internet

ya para importalo seria asi

"""

from colored import fg, bg, attr

"""
Importa un modulo que cambia el color de la salida
obviamente nescitamos leer la docucmentacion
para concer comollamar a cada componente

asi funciona con todos

otro ejemplo seria pandas
"""

from pandas import *
# es una libreria para procesar datos muy utilizada en ciencia de datos

"""
La mayoria de paquetes es recomendable
instalarlos en un ambiente especial env
de python para que no colisione con
otros archivos asi evitando errores
algo asi
"""

#python3 -m venv -Nombre-

#venv signifa virtual enviroment

#Otra forma seria instalando alguna imagen en docker


"""
Para considear una carpeta o directorio un
paquete o modulo, este mismo requiere tener
un archivo que se llama __init__.py

"""
