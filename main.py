from notification import find_all_subscribers, send_mail_to_subscibers
from sale_finder import PageScraper
from configuration_file import load_csv_to_price_dict


def main(page_scraper, price_dict):
    """
    The main flow of the program:
    1. Updating prices for all products in price_dict.
    2. Finds all subscribers in price_dict.
    3. Sends email notifications to subscribers.

    :param page_scraper: An instance of PageScraper.
    :param price_dict: Dictionary containing product and subscriber data.
    """
    price_dict = page_scraper.update_all_prices(price_dict)
    subscribers = find_all_subscribers(price_dict)
    send_mail_to_subscibers(subscribers, price_dict)


if __name__ == "__main__":
    """
    Entry point for the script. Loads data and starts the main process.
    """
    price_dict = load_csv_to_price_dict("product_overview.csv")
    page_scraper = PageScraper()
    main(page_scraper, price_dict)
