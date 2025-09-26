from notification import find_all_subscribers, send_mail_to_subscribers
from sale_finder import PageScraper
from utility_functions import load_csv_to_price_dict


def main(price_dict):
    page_scraper = PageScraper()
    price_dict = page_scraper.update_all_prices(price_dict)
    subscribers = find_all_subscribers(price_dict)
    send_mail_to_subscribers(subscribers, price_dict)


if __name__ == "__main__":
    price_dict = load_csv_to_price_dict("/app/product_overview.csv")
    main(price_dict)
