cliente = {'nombre': 'Luis', 'apellido': 'Aguilar', 'peso': 100, 'talla': 1.95}
consulta = (cliente['apellido'])
print(consulta)

# ------------------

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c3']['s2'])
"""para acceder a un valor especifico si hay otra estructura de datos
     es decir saber el valor exacto si hay una lista u otro diccionario, como en este ejemplo, donde se requiere saber el valor especifico dentro de una lista
     para esto se utilizaria, dos corchetes, [] para la clave y el segundo para el valor especifico dentro de ello.
"""

dicprueba = {'c1': ['a','b','c'], 'c2': ['d', 'e', 'f']}
print(dicprueba['c2'][1].upper())

# --------------------
dict = {1:'a', 2:'b'}
print(dict)
dict[3] = 'c'
print(dict)
dict[2] = 'B'
print(dict)

print(dict.keys()) # imprimira todas las claves
print(dict.values()) # imprimira todos los valores
print(dict.items()) # imprimira los items es decir {1:'a', 2:'b'}

# ----------------- Ejemplo de actualizacion de diccionario
mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}

mi_dic["pais"] = "Colombia"
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
print(mi_dic)

# cabe aclarar que podemos crar diccionarios por compresion como con las listas
cadena = "Luis alejandro aeiou aeiou aeiou"
vocales = ['a', 'e', 'i', 'o', 'u']
conteo = {vocal: cadena.count(vocal) for vocal in vocales}

print(conteo)

