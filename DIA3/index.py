mi_texto = "Esta es una prueba de indice"
# el segundo parametro es apartir de cual indice incia la buqueda y el tercero hasta cuando acaba
resultado = mi_texto.index("a", 1, 8)
print(resultado)

mi_texto = "Esta es una prueba de indice"
# el segundo parametro es apartir de cual indice incia la buqueda y el tercero hasta cuando acaba
resultado = mi_texto.rindex("a")  # busqueda inversa
print(resultado)

# con este, no necesitas acceder al .index, ya que solamente pide el numero que se desea saber que caracter esta ahi
mi_testo = "Esta es una prueba de indice"
resulta = mi_testo[6]
print(resulta)

