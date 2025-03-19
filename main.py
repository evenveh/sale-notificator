from notification import send_mail
from sale_finder import get_guitar_sales
from sale_comparator import compare_sales
import time

def main_loop():
    test = True
    old_guitars, url = get_guitar_sales()
    old_guitars = ['Ibanez EHB1505-SWL El-gitar: 25%', 'Ibanez GB10SE-BS George Benson: 10%', 'Ibanez S1070PBZ-CLB Elgitar: 10%', 'Ibanez TWP10: 10%']
    while test:
        guitars, url = get_guitar_sales()
        old_guitars = compare_sales(old_products=old_guitars, new_products=guitars, url = url)
        time.sleep(60*60)


if __name__ == "__main__":
    main_loop()
