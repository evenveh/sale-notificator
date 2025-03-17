from notification import send_mail
from sale_finder import get_guitar_sales


if __name__ == "__main__":
    guitars, url = get_guitar_sales()
    send_mail(guitars, url)
