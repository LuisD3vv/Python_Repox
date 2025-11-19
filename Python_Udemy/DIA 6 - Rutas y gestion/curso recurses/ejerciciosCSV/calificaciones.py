import csv
import os

nombre_salida = 'exportar.csv'
ruta = os.path.join(os.path.dirname(__file__),nombre_salida)

# datos para escribir en una lista de listas.
data = [
    ['Nombre','Apellido','Calificacion','Periodo'],
    ['Lissandro','Aguilar',9.5,2025],
    ['Eduardo','Aguilar',10,2024],
    ['William','Hernandez',9,2010],
    ['Luis','Mireles',10,2023],
]

with open (file=ruta,mode='w',encoding='utf8',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

print("Lectura bellaca")
with open (file=ruta,mode='r',encoding='utf8',newline='') as file:
    # Abrirlo en forma de clave: valor    
    csv_reader = csv.DictReader(file)
    print("")
    for row in csv_reader:
        print(row['Calificacion'])
        