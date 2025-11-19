import csv
import os
# este nos da la ruta actual
print(os.getcwd())

# para mejorar el uso de las rutas absoluta
ruta = os.path.join(os.path.dirname(__file__),'Inventory.csv')

# Para abrir correctamente los csv, debemos importar la libreria csv
# asi mismo, dentro de los parametros, a demas de la ruta y el modo, debemos de especificarle 
# la codificacion para que nop haya problema
try:
    with open(ruta, 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file)
        
        # Este metodo regresa una lista de filas en reader object
        for row in csv_reader:
            print(row)
            
            
except FileNotFoundError:
    print('error en el puto archivo')
# data_to_write = [
#     ['Name', 'Age', 'Grade'],
#     ['Alice', 25, 'A'],
#     ['Bob', 22, 'B'],
#     ['Charlie', 28, 'A+']
# ]

# newline nos asegura que las lineas se escribiran abajo de las que ya estan suponiendo que el modo de apertura lo permita
# try:
#     with open('Python_Udemy/DIA 6 - Rutas y gestion/curso recurses/csv/Output.csv', 'w', newline='') as file:
#         # Este metodo escribe en el csv
#         csv_writer = csv.writer(file)
#         csv_writer.writerows(data_to_write)
# except FileNotFoundError:
#     print('error en el puto archivo')