#Romario Guadalupe Limón Hernández

from bs4 import BeautifulSoup
import requests


linck = 'https://definicion.de/perro/'
respuesta = requests.get(linck)
contenido = respuesta.text


soup = BeautifulSoup(contenido, 'lxml')
#print(soup.prettify())

caja = soup.find('article', id="definicion-post-box", class_="post box-grey")

titulo = caja.find('a').get_text()
definicion = caja.find('div', class_="post-entry").get_text()

#print(titulo)
#print(definicion)

with open(f'{titulo}.txt', 'w') as file:
    file.write(definicion)