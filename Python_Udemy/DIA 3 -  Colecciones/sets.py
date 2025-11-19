mi_set = set([1,2,3,4,5]) # se necesita utilizar algun tipo de llave para que cuente como un elemento, solamente se puede mezclar con otras colecciones inmutables
print((len(mi_set)))

s1 = {1,2,3}
s2 = {3,4,5}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.add(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
#son colecciones que no admiten elementos repetidos, ademas que utilizan la misma metodologia de los conjuntos para sus elementos, como el join, diference y union

