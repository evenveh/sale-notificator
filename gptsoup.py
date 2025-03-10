import requests
from bs4 import BeautifulSoup


url = "https://evenstadmusikk.no/search?q=lagersalg&Filter=ProdusentID%C2%A41:ProdusentID%C2%A41_234%7CPrdGruppeLev2ID%C2%A41:PrdGruppeLev2ID%C2%A41_37%7CPrdGruppeLev1ID%C2%A41:PrdGruppeLev1ID%C2%A41_7"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    doc = BeautifulSoup(response.text, "html.parser")
    guitars = []
    products = doc.find_all("div", class_="WebPubElement pub-productlisting")
    for product in products:

        name_tag = product.find("span", class_="AddHeader1")
        name = name_tag.text.strip() if name_tag else "Unknown Guitar"

        guitars.append(name)

    for guitar in guitars:
        print(f"Name: {guitar}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
