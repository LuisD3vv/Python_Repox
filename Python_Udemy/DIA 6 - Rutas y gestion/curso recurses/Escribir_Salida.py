# Para abrir archivos nos basamos en la fucnion open, que toma dos parametros

# el archivo a leer y el modo de operacion, 

'''
a - append crea y pone el cursos al final
w - write crea y sobreescribe()
r - read solo lee
x - solo crea el archivo y da error en caso de existir
se pueden combinar modos
'''

lectura = open("mi_archivo.txt", 'a')

lectura.write("Nuevo inicio de sesión\n")

lectura.close()

lectura = open("mi_archivo.txt", 'r')

print(lectura.read())

lectura.close()

# Tambien se puede usar con el manejador de contextos with open as
print()
# no necesitamos cerrar el archivo
with open ("mi_archivo.txt", 'r') as lect:
    next(lect) # saltar cabecera, en algunos casos funciona
    if not lect:
        print("vacio")
    # imprime una linea
    print(lect.read())
    # imprime lineas en un rango, cada nueva impresion es una linea nueva
    print(lect.readline(),end='')
    # regresa una lista de los renglones
    print(lect.readlines(),end='')
    

# Tambien podemos iterar para escribir en

with open ("mi_archivo.txt", 'a') as lect:
    lect.writelines("Hola a la verga crack")
