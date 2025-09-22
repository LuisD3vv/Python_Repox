Mi_tuple = (1,2,(10,20),4)

Mi_tuple = list(Mi_tuple)
Mi_tuple = tuple(Mi_tuple)
print(type(Mi_tuple))
#---------------
t = (1, 2, 3, 1)
text_tuple =('luisito','vagina')
# es posible reasignar los valores solo si existe la misma cantidad de valores y variables
print(t.count(1))# requiere un parametro que es el valor que deseas saber que tanto aparece en el texto
print(t.index(2)) # localizar elemento
print(text_tuple.count(1))# requiere un parametro que es el valor que deseas saber que tanto aparece en el texto

# Las tuplas pueden distribuir el contenido entre otras variables yu desempaquetaras o no segun el caso

nombres = "Luis-Eduardo-jose-William"
# desempaquetado
(nombre1, *nombre2, nombre3) = nombres.split("-")
# Asi ignoramos el valor que no queremos con el guion bajo
(nombre1, nombre2, _, nombre3) = nombres.split("-")
print(nombre1, nombre2, nombre3)
# Tambien podemos crear una tupla con un solo valor, seria asi
tupla = (5,)
# es muy util saber esto porque los queries de las base de datos vienen  asi


