## Archivos CSV
### Como leer y escribir archivos.

>Los archivos csv o coma separated value, son archivos que como su nombre lo dice estan separadas con comas.

> en python podemos trabajar de manera sencilla ya sea con el modulo propiop csv o con pandas, para este ejemplo usaremos cvs

<pre> 
import cvs

with open(file='archivo.csv',mode= 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
</pre>

arriba esta lo mas basico para abrirlo, desde estos conceptos

>+ file es el nombre o ruta del archivo csv
>+ mode el modo de apertura, r,w,x,a
>+ encofind el modo de encodificacion del documento, es buena practica colocarlo en utf-8


<pre>
with open(file='archivo.csv',mode= 'r', encoding='utf8') as file:
    writer = csv.writer(file)
    writer = csv.writerows(a escribir)
</pre>

>Aqui, el argumento que le pasemos al writer, debera de ser una esteructra de datos como lista o uina lista de listas

<pre>
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
</pre>


#### Salida 
<pre> 
Nombre,Apellido,Calificacion,Periodo
Lissandro,Aguilar,9.5,2025
Eduardo,Aguilar,10,2024
William,Hernandez,9,2010
Luis,Mireles,10,2023
</pre>

como vemos cada lista es una fila del documento, al igual funciona de esta misma forma para la impresion
cada fila que iteremos es un renglon del documento csv original

### Como seleccionar columnas especificas

En el ejemplo de abajo lo que yo buscaba era la columna 4, que es la de ventas, por lo que utilice otra lista para guardar el contenido de esa columna, esto se logro con un 
len

<pre>
if len(row) > 4:
    # guardamos la columna de nuestro interes
    mayor_venta.append(row[4])
</pre>

asi se guarda solamente esa columna

>Book,Author,Original language,First published,sales in millions,Genre
<pre> 
try:
    with open(file=ruta,mode= 'r', encoding='utf8') as file:
        mayor_venta = [] # columna sales
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 4:
                # guardamos la columna de nuestro interes
                mayor_venta.append(row[4])
except FileNotFoundError:
    print(f"El archivo proporcionado no existe -> {file}")
</pre>

para rebobinar nuestro puntero hasta el inicio del documento
<pre>file.seek(0)</pre>