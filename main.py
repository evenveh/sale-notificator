from notification import send_mail, unwrap_product_string
from sale_finder import PageScraper
from sale_comparator import compare_products_on_page, create_message
import time
from get_secrets import get_secret


def initialization(page_scraper, url):
    initial_products_on_outlet = page_scraper.find_products_on_page(url)
    products_string = unwrap_product_string(initial_products_on_outlet)
    send_mail(message=f"Subject: Sale Notificator\n\nSale notificator is up and running!\n\n "
                      f"There are currently {len(initial_products_on_outlet)} guitars out: "
                      f"\n\n{products_string}\n\n URL: {url}")
    return initial_products_on_outlet


def main_loop(old_sales, url, page_scraper):
    while True:
        current_products_on_outlet = page_scraper.find_products_on_page(url)
        new_products_on_outlet, expired_products_on_outlet = compare_products_on_page(old_products=old_sales,
                                                                                      current_products=current_products_on_outlet)
        message = create_message(new_sales=new_products_on_outlet,
                                 expired_sales=expired_products_on_outlet,
                                 current_sales=current_products_on_outlet,
                                 url=url)
        send_mail(message)
        old_sales = current_products_on_outlet

        time.sleep(60 * 60 * 3)
        print("Starting new loop")


if __name__ == "__main__":
    url = get_secret("URL_IBANEZ_GUITARS_AND_BASS")
    page_scraper = PageScraper()
    initial_sales = initialization(page_scraper, url)
    main_loop(initial_sales, url, page_scraper)
