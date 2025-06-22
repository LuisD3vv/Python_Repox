"""
Para descargar modulos de internet, basta con 
buscar en internet el modulo que deseamos y
leer la documentacion de como funciona
lo descargamos de la siguiente manera

en mi caso como estoy en ubunto, requiero
de usar atp, si estas en windows puedes
usar directamente pip install paquete

yo utilice este

sudo apt install python3-nombre-del-paquete

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
""""

from pandas import *
# es una libreria para procesar datos muy utilizada en ciencia de datos

"""
La mayoria de paquetes es recomendable
instalarlos en un ambiente especial evn
de python para que no colisione con
otros archivos.

algo asi
"""

python3 -m venv -Nombre-

#venv signifa virtual enviroment