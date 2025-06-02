## _________________Overvåke priser___________________
# The configuration file includes a dictionary of products. Each product has a sub-dictionary with information:
# 1. URL - The URL of the product page
# 2. price_tag - The CSS selector to find the price on the product page
# 3. price - The current price of the product, initialized to 1.0, will be a dynamic value fetched from the website.


price_dict = {
    "Fiocchi 9mm 115 grs": {
        "url": "https://www.xxl.no/fiocchi-fiocchi-9mm-115-grs-fmj-ammunisjon/p/9000961_2_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["workaholix55@gmail.com", "even.vehus@gmail.com", "robin.frohaug@gmail.com"],
        "price": 1.0,
        "threshold": 155.0
    },
    "Fiocchi 9mm 124 grs": {
        "url": "https://www.xxl.no/fiocchi-cart-9-luger-fmj-124-ram-ammunisjon/p/1185862_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["workaholix55@gmail.com","robin.frohaug@gmail.com"],
        "price": 1.0,
        "threshold": 155.0
    },
    "CCI 22lr": {
        "url": "https://www.xxl.no/cci-cci-standard-22-lr-40gr-lrn-gun-rifle-ammunisjon/p/1189986_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["workaholix55@gmail.com"],
        "price": 1.0,
        "threshold": 55
    },
    "30-06": {
        "url": "https://www.xxl.no/fiocchi-30-06-springfield-147-fmj-ammunisjon/p/1147062_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["workaholix55@gmail.com"],
        "price": 1.0,
        "threshold": 200.0
    },
    "Fiocchi Steel 12/70": {
        "url": "https://www.xxl.no/fiocchi-fsteel-24g-hagleammunisjon/p/1224197_1_Style",
        "price_tag": '[data-testid="selling-price"]',
        "subscribers": ["workaholix55@gmail.com"],
        "price": 1.0,
        "threshold": 75.0
    }
}

# ___________Overvåke produkter på outletside___________
product_page_dict = {
    "Evenstad outlet": {
        "url": "https://evenstadmusikk.no/search?q=lagersalg&Filter=ProdusentID%C2%A41:ProdusentID%C2%A41_234|PrdGruppeLev1ID%C2%A41:PrdGruppeLev1ID%C2%A41_7",
        "product_class_name": "WebPubElement.pub-productlisting",
        "product_name_tag": "AddHeader1",
        "product_sale_tag": "YouSavePercentLabel",
        "subscribers": ["workaholix55@gmail.com"],
        "products_on_page": []  # Could be a dict also
}
}
