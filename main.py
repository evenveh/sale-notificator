import time
from notification import send_mail, unwrap_product_string
from sale_finder import PageScraper
from sale_comparator import compare_products_on_page, create_message
from get_secrets import get_secret


def initialization(scraper, url):
    """
    Initialize by scraping current products and ammunition price,
    then sending a startup notification email.
    """
    products = scraper.find_products_on_page(url)
    ammunition_price = scraper.fetch_item_price("https://www.xxl.no/fiocchi-fiocchi-9mm-115-grs-fmj-ammunisjon/p/9000961_2_Style")

    products_string = unwrap_product_string(products)
    message = (
        f"Subject: Sale Notificator\n\n"
        f"Sale notificator is up and running!\n\n"
        f"Test: There are currently {len(products)} guitars out:\n\n"
        f"{products_string}\n\n"
        f"URL: {url}\n\n"
        f"Ammunition price is: {ammunition_price} kr."
    )
    send_mail(message)
    return products, ammunition_price


def main_loop(previous_sales, url, scraper):
    """
    Continuously check for updates in sales and send notification emails.
    """
    while True:
        # Scrape current product data
        current_sales = scraper.find_products_on_page(url)
        new_sales, expired_sales = compare_products_on_page(
            old_products=previous_sales,
            current_products=current_sales
        )

        # Compose and send email with updates
        message = create_message(
            new_sales=new_sales,
            expired_sales=expired_sales,
            current_sales=current_sales,
            url=url
        )
        send_mail(message)

        # Update previous sales for the next iteration
        previous_sales = current_sales

        # Fetch and (optionally) log current ammunition price
        ammunition_price = scraper.fetch_item_price()

        print("Starting new loop")
        time.sleep(60 * 60 * 3)  # Sleep for 3 hours


if __name__ == "__main__":
    url = get_secret("URL_IBANEZ_GUITARS_AND_BASS")
    scraper = PageScraper()
    initial_sales, _ = initialization(scraper, url)
    main_loop(initial_sales, url, scraper)
