archivo = open("../curso recurses/prueba.txt", "w")
texto = input("Ingresa texto: ")
archivo.write(texto + "\n")
archivo.writelines(['Luis', 'Alejandro', 'Soberanes']) # Como lista

# Writelines funciona como una lista, por lo cual podemos meterle elementos por iteraciones
lista = ['Luis', 'Alejandro', 'Soberanes']

for nombre in lista:
    archivo.writelines(nombre + '\n')
archivo.close()

with open("../curso recurses/prueba.txt", "r") as archivo:
    print(archivo.read())

archivo = open("../curso recurses/prueba.txt", "a")
archivo.write("Log")
archivo.write(texto + "\n")