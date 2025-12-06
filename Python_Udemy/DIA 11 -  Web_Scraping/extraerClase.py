import bs4 # mejorar el formato
import requests # conectar y traer datos

# aqui guardamos la pagina/enlace que queremos pues
resultado = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")


sopa = bs4.BeautifulSoup(resultado.text,'lxml')


columna_lateral = sopa.select('.side_categories li')


# iterar sobre los elementos de la seccion de arriba
for li in columna_lateral:
    print(li.getText())
