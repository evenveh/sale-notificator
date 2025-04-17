from notification import send_mail, unwrap_product_string
from sale_finder import find_new_products
from sale_comparator import compare_sales, create_message
import time
from get_secrets import get_secret


def initialization():
    url = get_secret("URL_IBANEZ_GUITARS_AND_BASS")
    initial_sales = find_new_products(url)
    products_string = unwrap_product_string(initial_sales)
    send_mail(message=f"Subject: Sale Notificator\n\nSale notificator is up and running!\n\n "
                      f"There are currently {len(initial_sales)} guitars out: \n\n{products_string}\n\n URL: {url}")
    return initial_sales, url


def main_loop(old_sales, url):
    while True:
        current_sales = find_new_products(url)
        new_sales, expired_sales = compare_sales(old_products=old_sales, current_products=current_sales)
        message = create_message(new_sales=new_sales, expired_sales=expired_sales, current_sales=current_sales, url=url)
        send_mail(message)
        old_sales = current_sales

        time.sleep(60 * 60 * 3)
        print("Starting new loop")


if __name__ == "__main__":
    initial_sales, url = initialization()
    main_loop(initial_sales, url)
