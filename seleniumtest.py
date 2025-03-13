from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_guitar_sales():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    with webdriver.Chrome(service=service, options=chrome_options) as driver:

        url_Ibanez_guitars = "https://evenstadmusikk.no/search?q=lagersalg&Filter=ProdusentID%C2%A41:ProdusentID%C2%A41_234%7CPrdGruppeLev2ID%C2%A41:PrdGruppeLev2ID%C2%A41_37%7CPrdGruppeLev1ID%C2%A41:PrdGruppeLev1ID%C2%A41_7"
        url_Ibanez_guitars_and_bass="https://evenstadmusikk.no/search?q=lagersalg&Filter=ProdusentID%C2%A41:ProdusentID%C2%A41_234|PrdGruppeLev1ID%C2%A41:PrdGruppeLev1ID%C2%A41_7"
        url_all_guitars = "https://evenstadmusikk.no/search?Filter=PrdGruppeLev2ID%C2%A41:PrdGruppeLev2ID%C2%A41_37%7CPrdGruppeLev1ID%C2%A41:PrdGruppeLev1ID%C2%A41_7&q=lagersalg"
        url = url_Ibanez_guitars_and_bass
        driver.get(url)

        time.sleep(5)

        guitars = []
        products = driver.find_elements(By.CLASS_NAME, "WebPubElement.pub-productlisting")

        for product in products:
            try:
                name_tag = product.find_element(By.CLASS_NAME, "AddHeader1")
                name = name_tag.text.strip() if name_tag else "Unknown Guitar"

                sale_tag = product.find_element(By.CLASS_NAME, "YouSavePercentLabel")
                sale = sale_tag.text.strip() if sale_tag else "No discount"

                print(f"{name}: {sale}")
                guitars.append(f"{name}: {sale}")

            except Exception as e:
                print(f"Error: {e}")

    return guitars
