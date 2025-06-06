from notification import find_all_subscribers, send_mail_to_subscibers
from sale_finder import PageScraper
from time import sleep
from configuration_file import price_dict


def main_loop(page_scraper, price_dict):
    while True:
        price_dict = page_scraper.update_all_prices(price_dict)
        subscribers = find_all_subscribers(price_dict)
        send_mail_to_subscibers(subscribers, price_dict)

        sleep(60 * 60 * 24)


if __name__ == "__main__":
    page_scraper = PageScraper()
    main_loop(page_scraper, price_dict)
