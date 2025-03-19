import smtplib
from secrets import PASSWORD, TEST_EMAIL, RECIPIENT

def unwrap_product_string(products):
    product_string = "\n".join(products)
    return product_string

def send_mail(guitars, url):
    guitars_string = unwrap_product_string(guitars)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=TEST_EMAIL,
                            to_addrs=RECIPIENT,
                            msg = f"Subject: New or not new Ibanez guitars at Evenstad Outlet\n\nThere are currently {len(guitars)} guitars at Evenstad's outlet page:\n"
                                  f"{guitars_string}\n URL:" + url)

    print(f"An email has been sent to {RECIPIENT}")
