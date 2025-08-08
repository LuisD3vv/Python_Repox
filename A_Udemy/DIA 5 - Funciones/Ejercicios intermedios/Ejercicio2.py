"""
Lissandro AG 07/01/2025
"""
def unicas(palabra):  # Nombrar a la funcion y colocarle el parametro
    mi_set = set(palabra.lower()) # Convertir en set, automaticamente eliminara los duplicados
    clean = list(mi_set)  # Convertirla en lista para lograr utilizar el metodo sort()
    clean.sort() # Organizar la lista
    print(f"La palabra original '{palabra}', con las trasformaciones y en orden alfabetico\n es: {clean}")


unicas("cascarrabias")
