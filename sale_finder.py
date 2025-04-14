from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_sales(url):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())

    with webdriver.Chrome(service=service, options=chrome_options) as driver:

        driver.get(url)
        time.sleep(2)
        product_list = []
        product_class_name = "WebPubElement.pub-productlisting"
        products = driver.find_elements(By.CLASS_NAME, product_class_name)

        for product in products:
            try:
                name_tag = product.find_element(By.CLASS_NAME, "AddHeader1")
                name = name_tag.text.strip() if name_tag else "Unknown Guitar"

                sale_tag = product.find_element(By.CLASS_NAME, "YouSavePercentLabel")
                sale = sale_tag.text.strip() if sale_tag else "No discount"

                print(f"{name}: {sale}")
                product_list.append(f"{name}: {sale}")

            except Exception as e:
                print(f"Error: {e}")

    return product_list
