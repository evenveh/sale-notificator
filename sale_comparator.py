from notification import send_mail, unwrap_product_string


def compare_sales(old_products, new_products, url):
    if old_products == new_products:
        print("No changes in the sales.")
        return new_products
    else:
        for product in new_products:
            if product not in old_products:
                print(f"New product on sale: {product}")
                products_string = unwrap_product_string(new_products)

                send_mail(new_products, url)

        for product in old_products:
            if product not in new_products:
                print(f"Guitar no longer on sale: {product}")
                products_string = unwrap_product_string(new_products)

                send_mail(new_products, url)

    return new_products
