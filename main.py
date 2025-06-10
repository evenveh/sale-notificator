from notification import find_all_subscribers, send_mail_to_subscibers
from sale_finder import PageScraper
from configuration_file import load_csv_to_price_dict


def main(page_scraper, price_dict):
    price_dict = page_scraper.update_all_prices(price_dict)
    subscribers = find_all_subscribers(price_dict)
    send_mail_to_subscibers(subscribers, price_dict)


if __name__ == "__main__":
    price_dict = load_csv_to_price_dict("product_overview.csv")
    page_scraper = PageScraper()
    main(page_scraper, price_dict)
