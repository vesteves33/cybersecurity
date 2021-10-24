from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/321/riodejaneiro-rj").content

soup = BeautifulSoup(url, "html.parser")

temperatura = soup.find("span", class_="_margin-r-15")

print(temperatura.text)