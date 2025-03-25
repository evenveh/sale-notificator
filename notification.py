import smtplib
from secrets import PASSWORD, FROM_EMAIL, RECIPIENT
from get_secrets import get_secret

def unwrap_product_string(products):
    product_string = "\n".join(products)
    return product_string

def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=get_secret("FROM_EMAIL"), password=get_secret("PASSWORD"))
        connection.sendmail(from_addr=get_secret("FROM_EMAIL"),
                            to_addrs=get_secret("RECIPIENT"),
                            msg = message)

    print(f"An email has been sent to {get_secret("RECIPIENT")}")
