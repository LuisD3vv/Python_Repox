from  collections import defaultdict
cliente = {'nombre': 'Luis', 'apellido': 'Aguilar', 'peso': 97, 'talla': 1.95}
consulta = (cliente['apellido'])
print(consulta)

# ------------------

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c3']['s2'])
"""
  para acceder a un valor especifico si hay otra estructura de datos
  es decir saber el valor exacto si hay una lista u otro diccionario, como en este ejemplo, donde se requiere saber 
  el valor especifico dentro de una lista
  para esto se utilizaria, dos corchetes, [] 
  para la clave y el segundo para el valor especifico dentro de ello.
"""

dicprueba = {'c1': ['a','b','c'], 'c2': ['d', 'e', 'f']}
print(dicprueba["c2"][1].upper())

# --------------------
dict = {1:'a', 2:'b'}
dict2 = {3:'c', 4:'d'}
print(dict)
dict[3] = 'c'
print(dict)
dict[2] = 'B'
print(dict)

print(dict.keys()) # imprimira todas las claves
print(dict.values()) # imprimira todos los valores
print(dict.items()) # imprimira los items es decir {1:'a', 2:'b'}
print(dict.get(2)) # obtendra el valor de la clave en esa posicion
print(dict.update(dict2))
"""dict2.pop("nombre")
dict2.popitem("Elimina un clave valor")
dict2.clear("Eliminar el diccionario, se queda vacio")
dict2.setdefault("Nombre","Luis") # devuelve el valor de uina clave y si no existe la crea con otro valor
dict2.fromkeys(['a','b','c',1])# crea un diccionario nuevo con las clases dadas y el mismo valor para todas"""

# ----------------- Ejemplo de actualizacion de diccionario, ingresandole mas clave y sus valores al mismo tiempo
mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}

mi_dic["pais"] = "Colombia"
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
print(mi_dic)

# cabe aclarar que podemos crear diccionarios por comprehesion como con las listas
cadena = "Luis alejandro aeiou aeiou aeiou"
vocales = ['a', 'e', 'i', 'o', 'u']
conteo = {vocal: cadena.count(vocal) for vocal in vocales}

print(conteo)


# escuela = {}

# for i in range(1,3):
#   print("ingresa el nombre del estudiante")
#   alumno = input("Nombre: ")
#   for k in range(1,4):
#     calificaciones = float(input("Ingresa tus calificaciones: "))
#     escuela[alumno] = calificaciones

# for clave,valor in escuela.items():
#   print(clave, valor)


usuarios = {
  1: {"nombre":"Luis","edad": 21,"ciudad":"culiacan"},
  2: {"nombre":"eduardo","edad": 24,"ciudad":"culiacan"},
  3: {"nombre":"william","edad": 20,"ciudad":"culiacan"}
}
usuarios_nuevos = {
  4: {"nombre":"Diego","edad": 30,"ciudad":"Guadalajara"},
  5: {"nombre":"Samuel","edad": 21,"ciudad":"Peruvian"},
  6: {"nombre":"Francis","edad": 22,"ciudad":"Ohio"}

}
usuarios.update(usuarios_nuevos)
bucle = True
for clave, valor in usuarios.items():
  while bucle:
    try:
        buscar = int(input("Ingresa el id del perro: "))
        if buscar == -1:
          bucle = False
        elif buscar > len(usuarios):
          print("te saliste del rango perro")
    except:
      print("Porfavor ingresa un numero papuh")
    else:
      print(usuarios.get(buscar))


# Crear un diccionario default int donde la clave iniciara en 0
nombres = defaultdict(int)