#Outputs prueba (print())

#nombre = "Juan Pablo"
#apellidos = "Silva Romo"
#print("mi nombre es %s y mi apellido es %s"%(nombre, apellidos))

#import sys
#print(f"Buenos días {sys.argv[1]}")

from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen("https://es.wikipedia.org/wiki/Python")
html = response.read()

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()