import smtplib
from secrets import PASSWORD, TEST_EMAIL, RECIPIENT

def unwrap_guitar_string(guitars):
    guitars_string = "\n".join(guitars)
    return guitars_string

def send_mail(guitars, url):
    guitars_string = unwrap_guitar_string(guitars)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=TEST_EMAIL,
                            to_addrs=RECIPIENT,
                            msg = f"Subject: New Ibanez at Evenstad outlet\n\nThere are currently {len(guitars)} guitars at Evenstad's outlet page:\n"
                                  f"{guitars_string}\n URL:" + url)

    print(f"An email has been sent to {RECIPIENT}")
