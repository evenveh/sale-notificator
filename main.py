from notification import send_mail
from seleniumtest import get_guitar_sales


if __name__ == "__main__":
    guitars = get_guitar_sales()
    send_mail(guitars)
