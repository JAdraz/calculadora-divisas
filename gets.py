import requests
from bs4 import BeautifulSoup

def bcv_connection():
    # URL del BCV para obtener la tasa de cambio
    url = "https://www.bcv.org.ve/"

    # Realizar la solicitud GET al servidor y obtener el contenido HTML de la página
    session = requests.Session()
    response = session.get(url)
    content = response.content
    return content

def bcv_html():
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(bcv_connection(), "html.parser")

    # Encontrar el elemento que contiene la tasa de cambio
    tasa_element = soup.find("div", {"id" : "dolar"})

    # Extraer la tasa de cambio del elemento encontrado
    tasa_cambio = tasa_element.div.strong.text.strip() if tasa_element else "Tasa de cambio no encontrada"

    return tasa_cambio

def bcv_rate():
    # Eliminar la parte "Bs." del texto y cualquier otro caracter no numérico
    precio_numerico = ''.join(filter(str.isdigit, bcv_html().replace('.', '')))
        
    # Convertir el precio a tipo float dividiendo por 100
    precio_float = round(float(precio_numerico) / 100000000,2)

    return precio_float