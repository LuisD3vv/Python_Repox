import bs4
import requests

# Crear una url sin numero de pagina asociado
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# agreagar titulos con 4 o 5 estrellas

titulos_rating_alto = []

# Iterar paginas

for pagina in range(1,51):
    
    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')
    
    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    
    # iterar sobre cada libro
    
    for libro in libros:
        # verificar cantidad de estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            
            # guardar el titulo en una variable
            titulo_libro = libro.select('a')[1]['title']
            
            # agregar a la lista el libro que cumple con la condicion
            
            titulos_rating_alto.append(titulo_libro)
            
# ver libros
print("Titulos con mas de 4 estrellas.")
for t in titulos_rating_alto:
    print(t)