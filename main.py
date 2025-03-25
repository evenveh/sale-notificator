from notification import send_mail
from sale_finder import get_sales
from sale_comparator import compare_sales
import time
from get_secrets import get_secret

def main_loop():
    url = get_secret("URL_IBANEZ_GUITARS_AND_BASS")
    send_mail(message=f"Subject: Sale Notificator\n\nSale notificator is up and running!\n\n url:\n{url}")
    old_guitars = get_sales(url)

    while True:
        guitars = get_sales(url)
        old_guitars = compare_sales(old_products=old_guitars, new_products=guitars, url = url)
        time.sleep(60*60*3)

if __name__ == "__main__":
    main_loop()
