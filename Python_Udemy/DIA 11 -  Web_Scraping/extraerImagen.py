import bs4 # mejorar el formato
import requests # conectar y traer datos
from selenium import webdriver # para javascript, investigar despues

# aqui guardamos la pagina/enlace que queremos pues
resultado = requests.get("https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1")


sopa = bs4.BeautifulSoup(resultado.text,'lxml')

# seleccionar el atributo src del primer elemento con tal nombre de clase
clase = sopa.select('.ProductImage')[0]['src']
print(clase)

imagen_curso_1 = requests.get(clase)

# escribrir imagen en binario, con el contenido de la variable, basicamente creamos una imagen con el contenido binario sacado de la pagina
f = open('/home/lissandro/Python_Repox/Python_Udemy/DIA 11 -  Web_Scraping/mi_imagen.jpg','wb')
f.write(imagen_curso_1.content)
f.close()