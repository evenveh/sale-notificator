from notification import send_mail
from sale_finder import get_guitar_sales
from sale_comparator import compare_sales
import time

def main_loop():
    test = True
    old_guitars, url = get_guitar_sales()

    while test:
        guitars, url = get_guitar_sales()
        old_guitars = compare_sales(old_products=old_guitars, new_products=guitars, url = url)
        send_mail(guitars, url)
        time.sleep(60*60)


if __name__ == "__main__":
    main_loop()
