from notification import send_mail, unwrap_product_string
from sale_finder import get_sales
from sale_comparator import compare_sales
import time
from get_secrets import get_secret


def initialization():
    url = get_secret("URL_IBANEZ_GUITARS_AND_BASS")
    initial_sales = get_sales(url)
    products_string = unwrap_product_string(initial_sales)
    send_mail(message=f"Subject: Sale Notificator\n\nSale notificator is up and running!\n\n "
                      f"There are currently {len(initial_sales)} guitars out: \n\n{products_string}\n\n URL: {url}")
    return initial_sales, url


def main_loop(old_guitars, url):
    while True:
        guitars = get_sales(url)
        compare_sales(old_products=old_guitars, new_products=guitars, url=url)
        old_guitars = guitars
        time.sleep(60 * 60 * 3)
        print("Starting new loop")


if __name__ == "__main__":
    initial_sales, url = initialization()
    main_loop(initial_sales, url)
