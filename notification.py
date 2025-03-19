import smtplib
from secrets import PASSWORD, TEST_EMAIL, RECIPIENT

def unwrap_product_string(products):
    product_string = "\n".join(products)
    return product_string

def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=TEST_EMAIL,
                            to_addrs=RECIPIENT,
                            msg = message)

    print(f"An email has been sent to {RECIPIENT}")
