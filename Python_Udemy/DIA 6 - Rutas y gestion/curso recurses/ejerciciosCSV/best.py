import csv
import os
print(os.getcwd())

# trabajar con rutas absolutas siempre sera mejor opcion
ruta = os.path.join(os.path.dirname(__file__),'Bestseller .csv')
rutacompleta = os.path.dirname(__file__)
#csv/inventory.csv

os.system("clear")
'''
necesito hacer una busqueda por el libro que tenga
mas ventas y guardar su indice para guardarlo en otra lista 
y agregarlo al csv nuevo
'''
## Hay que tener cuidadado a la hora de trabajar con comparaciones numericas
## convertirlas primero antes de realizar operacion
def mayor(lista: list):
    mayor = lista[1]
    for venta in lista:
        if venta == str(venta):
            continue
        # casteo a numeros para hacer comparaciones
        if float(venta) > float(mayor):
            mayor = venta
    return mayor

# guardamos el libro

book = []
try:
    with open(file=ruta,mode= 'r+', encoding='utf8') as file:
        columna_ventas= [] # columna sales
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 4:
                # guardamos la columna de nuestro interes
                columna_ventas.append(row[4]) 
        # volver al inicion del documento (rebobinar) truncate lo lee hasta la parte indicada en el ()
        file.seek(0)# lo coloca al inicio mas no lo lee automaticamente
        # por eso aqui se vuelve a leer
        reader = csv.reader(file)
        for fila2 in reader:
            if mayor(columna_ventas) in fila2:
                book.append(fila2)
                break # se termina a la primera coincidencia porque se supone que ya se reviso que sea el mayor.
except FileNotFoundError:
    print(f"El archivo proporcionado no existe -> {file}")

with open (os.path.join(rutacompleta,'bestseller_info.csv'),'w',encoding='utf8' ) as file:
    writer = csv.writer(file)
    writer.writerows(book)

'''
No se debe de usar el mismo puntero para
leer y escribir, debemos reposicionar primero
con seek para evitar problemas ya que ambos
usan el msimo buffer.
'''