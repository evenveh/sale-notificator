from notification import unwrap_product_string, send_mail


def create_message(new_products, old_products, current_products, url):

    if new_products and old_products:
        new_products_string = unwrap_product_string(new_products)
        old_products_string = unwrap_product_string(old_products)
        print("Sending message about both new and expired products")
        msg = f"Subject: Update on sales\n\n There are both new and expired products.\n\n New products: {new_products_string}\n\n Expired products:{old_products_string} \n\nURL: {url}"
        send_mail(message=msg)

    if new_products and not old_products:
        new_products_string = unwrap_product_string(new_products)
        print("Sending message about new product")
        msg = f"Subject: New Ibanez guitar at Evenstad Outlet\n\nThere is a new product on Evenstad's outlet page: {new_products_string}. \n There are currently {len(new_products)} guitars out: \n\n{unwrap_product_string(current_products)}\n\n URL: {url}"
        send_mail(message=msg)

    if old_products and not new_products:
        old_products_string = unwrap_product_string(new_products)
        print("Sending message about product no longer for sale")
        msg = f"Subject: Product no longer for sale at Evenstad's Outlet\n\n The product: {old_products_string} is no longer for sale. \n There are currently {len(new_products)} guitars out: \n\n{unwrap_product_string(current_products)}\n\n URL: {url}"
        send_mail(message=msg)

    else:
        return


def compare_sales(old_products, current_products):
    new_products_list = []
    old_products_list = []
    if old_products == current_products:
        print("No change in the sales.")
        return new_products_list, old_products_list
    else:
        for product in current_products:
            if product not in old_products:
                new_products_list.append(product)
        for product in old_products:
            if product not in current_products:
                old_products_list.append(product)

    return new_products_list, old_products_list
