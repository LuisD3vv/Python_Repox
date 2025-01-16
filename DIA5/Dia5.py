import random

# importar choice
# funciones para pedir letra, validar letra, chequear letra, si gano o no
# primero escribir funciones y luego ponerle codigo

lista_palabras = ['luis',
                  'guerra',
                  'pepino',
                  'gato',
                  'sabina',
                  'televisor',
                  'galleta',
                  'solo']

palabra_aleatoria = random.choice(lista_palabras) # Tomar una palabra aleatoria.
palabra_aleatoria = list(palabra_aleatoria)

nueva_lista = ['-' if i < len(palabra_aleatoria) else item for i, item in enumerate(palabra_aleatoria)]
print(f"La palabra contiene la siguiente cantidad de caracteres {nueva_lista}")











# def intento_usuario(palabra, palabra_aleatoria): # necesita ambos parametros, el intento del usuario y la palabra original
#
#     for l in palabra_aleatoria
# intento_usuario(input('ingresa tu intento: '), palabra_aleatoria)
# def validar_letra():
#
# def palabra_in():
#
# def win_lose();




# while