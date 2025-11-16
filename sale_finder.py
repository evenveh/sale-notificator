from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from utility_functions import domain_and_key_mapper

class PageScraper:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.service = Service(ChromeDriverManager().install())

    def find_products_on_page(self,
                              url,
                              product_class_name="WebPubElement.pub-productlisting",
                              product_name_tag="AddHeader1",
                              product_sale_tag="YouSavePercentLabel"
                              ):

        with webdriver.Chrome(service=self.service, options=self.chrome_options) as driver:

            product_list = []
            product_dict = {}
            driver.get(url)
            time.sleep(2)
            products = driver.find_elements(By.CLASS_NAME, product_class_name)

            for product in products:
                try:
                    name_tag = product.find_element(By.CLASS_NAME, product_name_tag)
                    name = name_tag.text.strip() if name_tag else "Unknown Product"

                    sale_tag = product.find_element(By.CLASS_NAME, product_sale_tag)
                    sale = sale_tag.text.strip() if sale_tag else "No discount"

                    print(f"{name}: {sale}")
                    product_list.append(f"{name}: {sale}")
                    product_dict[name] = sale

                except Exception as e:
                    print(f"Error: {e}")

        return product_list

    def fetch_item_price(self,
                         url,
                         price_tag):

        with webdriver.Chrome(service=self.service, options=self.chrome_options) as driver:
            price = None
            try:
                driver.get(url)
                wait = WebDriverWait(driver, 5)
                price_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, price_tag)))
                price_text = price_element.get_attribute("textContent").split("pr")[0].strip()

                cleaned_text = re.sub(r'[^\d,\.]', '', price_text)
                cleaned_text = cleaned_text.replace(',', '.')
                price = float(cleaned_text)

            except Exception as e:
                print(f"Error: {e}")

        return price

    def update_all_prices(self, price_dict):
        for product, details in price_dict.items():
            price = self.fetch_item_price(url=details["url"],
                                          price_tag=domain_and_key_mapper(url=details["url"]))
            details["price"] = price
            print(f"{product}: {price}kr")
        return price_dict
