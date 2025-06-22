mi_tuple = (1,2,(10,20),4)

mi_tuple = list(mi_tuple)
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))
#---------------
t = (1,2,3, 1)
text_tuple =('luisito','vagina')
# es posible reasiganr los valores solo si existe la misma cantidad de valores y variables
print(t.count(1))# requiere un parametro que es el valor que deseas saber que tanto aparece en el texto
print(t.index(2)) # localizar elemento
print(text_tuple.count(1))# requiere un parametro que es el valor que deseas saber que tanto aparece en el texto
