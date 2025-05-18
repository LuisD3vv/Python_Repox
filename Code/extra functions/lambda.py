#Funciones anonimas, se declaran asi
lista = [1,2,3,4,5,6,7,8,9,0]

luis = map(lambda n: n % 2== 0, lista)

#utilizandolo junto a la funcion map, y lambda requiere parametro, y condicion
# ya el iterable es de map
print(list(luis))


