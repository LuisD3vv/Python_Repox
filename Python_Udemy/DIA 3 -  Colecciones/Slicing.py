texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:3]  # este metodo es conocido como slicing
# los primeros dos puntos despues del primer valor, se le toma como un hasta, es decir muestrame los valores del 2 hasta el 10 sin incluir el 10, si solo se ponen los puntos, este continuara hasta el final es decir [2:]
# si no se pone el segunod valor es decir [:10] zse topmara como inicia desde el principio y para en el cinco,
# posteriormente los el segundo valor es decir, en este caso el 3, seria los pasos o saltos que etaria dando a la cadena dada (substring)
# es decir, del 2 a 10, con saltos cada 2 caracteres
print(fragmento)

# inicia desde el comienzo bien y termina en el 9(no incluye el 10)
texto = "ABCDEFGHIJKLM"
fragmento = texto[:10:3]
print(fragmento)

# imprime toda la lista con saltos de 3
texto = "ABCDEFGHIJKLM"
fragmento = texto[::3]
print(fragmento)

# basicamente imprime todo
texto = "ABCDEFGHIJKLM"
fragmento = texto[::]
print(fragmento)

# recorte al reves

texto = "Luisito"
fragmento = texto[:10:-1]
print(fragmento)
