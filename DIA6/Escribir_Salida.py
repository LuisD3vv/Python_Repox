lectura = open("mi_archivo.txt", 'a')

lectura.write("Nuevo inicio de sesión\n")

lectura.close()

lectura = open("mi_archivo.txt",'r')

print(lectura.read())

lectura.close()