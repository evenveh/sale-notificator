import smtplib
from os import getenv

def unwrap_product_string(products):
    product_string = "\n".join(products)
    return product_string

def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=getenv("FROM_EMAIL"), password=getenv("PASSWORD"))
        connection.sendmail(from_addr=getenv("FROM_EMAIL"),
                            to_addrs=getenv("RECIPIENT"),
                            msg = message)

    print(f"An email has been sent to {getenv("RECIPIENT")}")
