from sale_finder import get_sales
from sale_comparator import compare_sales
from secrets import URL_ALL_GUITARS, URL_IBANEX_GUITARS, URL_IBANEZ_GUITARS_AND_BASS
import time

def main_loop():
    url = URL_IBANEZ_GUITARS_AND_BASS
    test = True
    old_guitars = get_sales(url)
    while test:
        guitars = get_sales(url)
        old_guitars = compare_sales(old_products=old_guitars, new_products=guitars, url = url)
        time.sleep(60*60*3)

if __name__ == "__main__":
    main_loop()
