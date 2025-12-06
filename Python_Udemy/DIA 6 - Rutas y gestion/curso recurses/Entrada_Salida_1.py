# Ejemplo sencillo de lectura
# existen 3 diferentes tipos de archivo r,a y w
"""
'r' sirve para leer el archivo e imprimir sus lineas
"a" sirve para escribir al ultimo del elemento, util para hacer logs
"w" sirve para modificar o crear un archivo. si no existe al momento de crearla, este lo creara automaticamente
"""
lectura = open("../prueba.txt", 'r')
for line in lectura:
    print(line)
print(lectura.read(), end=" ")

lectura.close()  # buena practica. / aparte necesaria jajaj

print("con open \n")
# Otra forma que lee y cierra actomaticamente cuadno se deja de leer el archivo
with open("../prueba.txt", 'r') as lecturita:
    print(lecturita.readlines()) # Regresa una linea

# Por cosecuencia todos lo metodos de string se pueden utilzar.

lineas = []
while True:
    linea = input()
    if linea.upper() == "FIN":
        break
    lineas.append(linea)

contenido = "\n".join(lineas)
print(contenido)
