from notification import send_mail, unwrap_product_string
from sale_finder import get_sales
from sale_comparator import compare_sales
import time
from get_secrets import get_secret


def initialization():
    url = get_secret("URL_IBANEZ_GUITARS_AND_BASS")
    old_guitars = get_sales(url)
    products_string = unwrap_product_string(old_guitars)
    send_mail(message=f"Subject: Sale Notificator\n\nSale notificator is up and running!\n\n "
                      f"There are currently {len(old_guitars)} guitars out: \n\n{products_string}\n\n URL: {url}")
    return old_guitars, url


def main_loop(old_guitars, url):
    while True:
        guitars = get_sales(url)
        old_guitars = compare_sales(old_products=old_guitars, new_products=guitars, url=url)
        time.sleep(60 * 60 * 3)
        print("Starting new loop")


if __name__ == "__main__":
    old_guitars, url = initialization()
    main_loop(old_guitars, url)
