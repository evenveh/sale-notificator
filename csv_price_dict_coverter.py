import csv


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
                "price_tag": row["Price Tag"],
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
