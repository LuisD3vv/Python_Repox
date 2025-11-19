mi_set = set([1,2,3,4,5]) # se necesita utilizar algun tipo de llave para que cuente como un elemento, solamente se puede mezclar con otras colecciones inmutables
print((len(mi_set)))

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#son colecciones que no admiten elementos repetidos,

a= {2,4,6,8,10}
b= {1,3,6,9}

# agregar elementos o buscar, no elimina por indices, si no la aparicion de tal elemento

a.add(2)
a.remove(2)

#ademas que utilizan la misma metodologia de los conjuntos para sus elementos, como el join, diference y union


print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.discard(b))
print(a.difference_update(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))

# No admite repetidos

setrepetido = {1,2,2,3,4,5,6,7,8,9}
print(setrepetido)

