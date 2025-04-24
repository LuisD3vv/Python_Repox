from pathlib import Path

lectura = open("nombres.txt", "r")

# devuelve una lista
print(lectura.readlines())

# lee el archivo completo
print(lectura.read())
# le una linea
print(lectura.readline())

lectura.close()

