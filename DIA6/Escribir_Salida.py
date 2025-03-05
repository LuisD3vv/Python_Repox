lectura = open("mi_archivo.txt", 'a')

lectura.write("Nuevo inicio de sesión")

lectura.close()

lectura = open("mi_archivo",'r')

print(lectura.read())

lectura.close()