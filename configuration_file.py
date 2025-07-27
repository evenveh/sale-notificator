import csv

price_dict = {
    "Fiocchi 9mm 115 grs": {
        "url": "https://www.xxl.no/fiocchi-fiocchi-9mm-115-grs-fmj-ammunisjon/p/9000961_2_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["even.vehus@gmail.com", "robin.frohaug@gmail.com"],
        "price": 1.0,
        "threshold": 155.0
    },
    "Fiocchi 9mm 124 grs": {
        "url": "https://www.xxl.no/fiocchi-cart-9-luger-fmj-124-ram-ammunisjon/p/1185862_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["even.vehus@gmail.com", "robin.frohaug@gmail.com"],
        "price": 1.0,
        "threshold": 155.0
    },
    "CCI 22lr": {
        "url": "https://www.xxl.no/cci-cci-standard-22-lr-40gr-lrn-gun-rifle-ammunisjon/p/1189986_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["even.vehus@gmail.com", "eskil.vehus@gmail.com"],
        "price": 1.0,
        "threshold": 55
    },
    "30-06": {
        "url": "https://www.xxl.no/fiocchi-30-06-springfield-147-fmj-ammunisjon/p/1147062_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["even.vehus@gmail.com", "eskil.vehus@gmail.com"],
        "price": 1.0,
        "threshold": 200.0
    },
    "Fiocchi Steel 12/70": {
        "url": "https://www.xxl.no/fiocchi-fsteel-24g-hagleammunisjon/p/1224197_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["even.vehus@gmail.com", "eskil.vehus@gmail.com"],
        "price": 1.0,
        "threshold": 75.0
    },

    "Sykkelbukse, svart, herre": {
        "url": "https://www.xxl.no/gore-wear-c3-ws-bibtights-w-pad-22-23-sykkelbukse-herre-svart/p/1150289_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["steinar@vehus.com"],
        "price": 1.0,
        "threshold": 1000.0
    },

    "100 % Whey Protein 3 kg, proteinpulver": {
        "url": "https://www.xxl.no/proteinfabrikken-100-whey-protein-3-kg-proteinpulver/p/1093331_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["even.vehus@gmail.com"],
        "price": 1.0,
        "threshold": 700
    },
}

# ___________Products on outlet page___________
product_page_dict = {
    "Evenstad outlet": {
        "url": "https://evenstadmusikk.no/search?q=lagersalg&Filter=ProdusentID%C2%A41:ProdusentID%C2%A41_234|PrdGruppeLev1ID%C2%A41:PrdGruppeLev1ID%C2%A41_7",
        "product_class_name": "WebPubElement.pub-productlisting",
        "product_name_tag": "AddHeader1",
        "product_sale_tag": "YouSavePercentLabel",
        "subscribers": ["workaholix55@gmail.com"],
        "products_on_page": {}
    }
}



#_________Some utility functions to convert the price dictionary as csv, and convert a csv to a price dictionary_________
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