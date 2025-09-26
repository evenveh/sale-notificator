import csv
from urllib.parse import urlparse


def load_csv_to_price_dict(filename="price_dict.csv"):
    """
    Converts a CSV file back into a dictionary identical to the original price_dict.

    :param filename: Name of the CSV file to read the data from.
    :return: A dictionary containing product details.
    """
    price_dict = {}
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            price_dict[row["Product Name"]] = {
                "url": row["URL"],
                "subscribers": row["Subscribers"].split(", "),
                "price": float(row["Price"]),
                "threshold": float(row["Threshold"])
            }
    return price_dict


def save_price_dict_to_csv(price_dict, filename="price_dict.csv"):
    """
    Saves the price_dict dictionary to a CSV file.

    :param price_dict: Dictionary containing product details.
    :param filename: Name of the CSV file to save the data.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["Product Name", "URL", "Price Tag", "Subscribers", "Price", "Threshold"])

        # Write the data rows
        for product, details in price_dict.items():
            writer.writerow([
                product,
                details["url"],
                details["price_tag"],
                ", ".join(details["subscribers"]),
                details["price"],
                details["threshold"]
            ])


def identify_domain(url):
    parsed = urlparse(url)
    return parsed.hostname


def domain_and_key_mapper(url):
    domain = identify_domain(url)

    with open("/app/page_configuration.csv", newline="") as f:
        reader = csv.DictReader(f)
        domain_key_map = {row["Domain"]: row["Key"] for row in reader}

    if domain in domain_key_map:
        return domain_key_map[domain]
    else:
        raise ValueError(f"Domain '{domain}' not found in configuration. Maybe the domain has not been configured yet? "
                         f"Try adding it to page_configuration.csv.")
