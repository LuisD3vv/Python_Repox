archivo = open("prueba.txt", "w")
texto = input("Ingresa texto: ")
archivo.write(texto)
archivo.writelines(['Luis', 'Alejandro', 'Soberanes'])

lista = ['Luis', 'Alejandro', 'Soberanes']

for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

with open("prueba.txt", "r") as archivo:
    print(archivo.read())

archivo = open("prueba.txt", "a")
archivo.write("Log")
archivo.write(texto)