from notification import send_mail, unwrap_product_string

def create_message(new_products, old_products, url):
    if new_products & old_products:
        message = f"Subject: Update on sales\n\n New products.... Expired products...URL: {url}"
        print("Sending message about product no longer for sale")

    if new_products and not old_products:
        products_string = unwrap_product_string(new_products)
        message = f"Subject: New Ibanez guitar at Evenstad Outlet\n\nThere is a new product on Evenstad's outlet page: {product}. \n There are currently {len(new_products)} guitars out: \n\n{products_string}\n\n URL: {url}"
        print("Sending message about new product")
        send_mail(message)

    if old_products and not new_products:
        products_string = unwrap_product_string(new_products)
        message = f"Subject: Product no longer for sale at Evenstad's Outlet\n\n The product: {product} is no longer for sale. \n There are currently {len(new_products)} guitars out: \n\n{products_string}\n\n URL: {url}"
        print("Sending message about product no longer for sale")
        send_mail(message)


def compare_sales(old_products, new_products):
    new_products = []
    old_products = []
    if old_products == new_products:
        print("No change in the sales.")
        return new_products
    else:
        for product in new_products:
            if product not in old_products:
                new_products.append(product)
        for product in old_products:
            if product not in new_products:
                old_products.append(product)

    return new_products, old_products