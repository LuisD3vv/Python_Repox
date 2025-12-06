# librerias luego le pongo para que se necesitan
import bs4 # mejorar el formato
import requests # conectar y traer datos

# aqui guardamos la pagina/enlace que queremos pues
resultado = requests.get("https://www.escueladirecta.com/")

print(resultado.text)

# texto y motor de conversion html
sopa = bs4.BeautifulSoup(resultado.text,'lxml') # o html
print(sopa)
# seleccionar una etiqueta
print(sopa.select('title'))
parrafoEspecial = sopa.select('title')[0].getText() # solo el texto sin la etiqueta

# despues de traer los elementos, podemos utilizar los metodos de listas.
parrafos = sopa.select('p')[3].getText()
print(parrafos)
# cantidad de veces
print(len(sopa.select('p')))
