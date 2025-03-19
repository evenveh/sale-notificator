from notification import send_mail


def compare_sales(old_products, new_products):
    if old_products == new_products:
        print("No changes in the sales.")
        return new_products
    else:
        for product in new_products:
            if product not in old_products:
                print(f"New product on sale: {product}")

        for product in old_products:
            if product not in new_products:
                print(f"Guitar no longer on sale: {product}")

    return new_products
