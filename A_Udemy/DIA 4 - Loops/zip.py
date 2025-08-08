# * La funcion zip nos ayuda a tomar una avriedad de iterables(listas, Tuples, diccionario, etc) y los agrupa en tuples
nombres = ['Luis', 'Eduardo', 'Valeria', 'William']
edades = [20, 23, 19, 19]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombres, edades, ciudades))

print(combinados)

for nombre, edades, ciudades in combinados:
    print(f'{nombre} tiene {edades} años y vive en {ciudades}')

