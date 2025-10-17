import re


texto = "Si necesitas ayuda llama al (658)-598-9977 las 2 horas al servicio de ayuda online"

# forma antigua

palabra = "ayuda" in texto
print(palabra)

patron = 'ayuda'

busqueda = re.search(patron,texto)
# Esto es una lista
#busquedaTodo = re.findall(patron,texto)
for hallazgo in re.finditer(patron,texto): # para buscar coincidencias dentro de un iterador
    print(hallazgo.span())

print(busqueda.span())
print(busqueda.start())
print(busqueda.end())
print(busqueda.groups()) # el conjunto de todos los elementos del patron
# cada objeto de busqueda tiene sus propias propiedades

tel = "llama al 545-343-2323 ya mismo"

# contruyendo asi el patron, podemos acceder a cada uno de los grupos de la cadena

# Es decir el grupo(1) es la primera coindicencia que se cumple del patron, en este caso los primeros
# 3 numeros
patron2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron2,tel) # / group

# con .group vemos el resultado como tal


print(resultado.group())



clave = input("Clave: ")

# como deberia de estar estructurado la entrada
patron3 = r'\D{1}\w{7}'

chequear = re.search(patron3,clave)
print(chequear)


aviso = "No atendemos los lunes"

buscar = re.search(r'lunes|martes',aviso) # el pipeline funciona como or aqui


buscar2 = re.search(r'demos',aviso)


# Coincidencia al inicio o final de la cadena

iniciaCon = re.search(r'^\D',aviso)
terminaCon = re.search(r'\D$',aviso)

# cadenas para excluir [lo que este aqui dentro se escluye]

iniciaCon = re.findall(r'[^\s]+',aviso)

print(" ".join(iniciaCon))

# conjunto de coincicencias

patronumerico = r'[0-9]' # equivalente a \d
patroAlfabetico = r'[a-zA-Z]'

# ejemplo

vocales = r'[aeiou]' # esto buscara cualquier coinciencia completa que contenga esta palabra, no una por una, en es caso se usaria or o pipeline

negacion = r'[^0-9] | [^a-zA-z]' # equivalente a |D


# para esto nos puede ayudar
# rjust(rellenar a la izquierda ocn cualquier caracter), zfill(rellenar a la izquierda solo con ceros)