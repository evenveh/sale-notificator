from notification import send_mail, unwrap_product_string, craft_message_for_updated_prices
from sale_finder import PageScraper
from sale_comparator import compare_products_on_page, create_message
import time
from get_secrets import get_secret
from configuration_file import price_dict


def update_all_prices(page_scraper):
    for product, details in price_dict.items():
        price = page_scraper.fetch_item_price(url=details["url"],
                                              price_tag=details["price_tag"])
        details["price"] = price
        print(f"{product}: {price} NOK")
    return price_dict


def main_loop(page_scraper):
    while True:
        price_dict = update_all_prices(page_scraper)
        message = craft_message_for_updated_prices(price_dict)
        send_mail(message)

        time.sleep(60 * 60 * 24)


if __name__ == "__main__":
    page_scraper = PageScraper()
    initial_sales = main_loop(page_scraper)
