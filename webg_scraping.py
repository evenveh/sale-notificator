from bs4 import BeautifulSoup
import requests
import re

url = ("https://evenstadmusikk.no/search?q=lagersalg&Filter=ProdusentID%C2%A41:ProdusentID%C2%A41_234%7CPrdGruppeLev2ID%C2%A41:PrdGruppeLev2ID%C2%A41_37%7CPrdGruppeLev1ID%C2%A41:PrdGruppeLev1ID%C2%A41_7")
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

div = doc.find(id = "A100113F670N1000044")

items = div.find_all(string = re.compile("Ibanez"))

print(items)

for item in items:
    print(item)
