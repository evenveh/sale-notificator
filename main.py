from notification import send_mail, craft_message_for_updated_prices, sort_recipients_and_subscriptions
from sale_finder import PageScraper
import time
from configuration_file import price_dict


def update_all_prices(page_scraper):
    for product, details in price_dict.items():
        price = page_scraper.fetch_item_price(url=details["url"],
                                              price_tag=details["price_tag"])
        details["price"] = price
        print(f"{product}: {price} NOK")
    return price_dict


def main_loop():
    page_scraper = PageScraper()

    while True:
        price_dict = update_all_prices(page_scraper)
        subscribers = sort_recipients_and_subscriptions(price_dict)

        for subscriber in subscribers:
            message = craft_message_for_updated_prices(price_dict, subscriber)
            send_mail(message)
            time.sleep(10)

        time.sleep(60 * 60 * 24)


if __name__ == "__main__":
    main_loop()
