from notification import send_mail
from sale_finder import get_guitar_sales
import time

def main_loop():
    test = True
    while test:
        guitars, url = get_guitar_sales()
        send_mail(guitars, url)
        time.sleep(60*60)


if __name__ == "__main__":
    main_loop()