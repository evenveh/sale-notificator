from notification import send_mail, unwrap_product_string

def compare_sales(old_products, new_products, url):
    if old_products == new_products:
        print("No changes in the sales.")
        return new_products
    else:
        for product in new_products:
            if product not in old_products:
                msg = f"New product on sale: {product}"
                products_string = unwrap_product_string(new_products)
                message = f"Subject: New Ibanez guitars at Evenstad Outlet\n\nThere is a new product on Evenstad's outlet page: {product}. \n There are currently {len(new_products)} guitars out: \n{products_string}\n\n URL: {url}"

                send_mail(message)

        for product in old_products:
            if product not in new_products:
                msg = f"Guitar no longer on sale: {product}"
                products_string = unwrap_product_string(new_products)
                message = f"Subject: Product no longer for sale at Evenstad's Outlet\n\n The product: {product} is no longer for sale. \n There are currently {len(new_products)} guitars out: \n{products_string}\n\n URL: {url}"

                send_mail(message)

    return new_products
