from notification import find_all_subscribers, send_mail_to_subscibers
from sale_finder import PageScraper
from time import sleep
from configuration_file import load_csv_to_price_dict


def main_loop(page_scraper, price_dict):
    while True:
        price_dict = page_scraper.update_all_prices(price_dict)
        subscribers = find_all_subscribers(price_dict)
        send_mail_to_subscibers(subscribers, price_dict)

        sleep(60 * 60 * 12)


if __name__ == "__main__":
    price_dict = load_csv_to_price_dict("price_dict.csv")
    page_scraper = PageScraper()
    main_loop(page_scraper, price_dict)
