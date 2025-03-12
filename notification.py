import smtplib
from Secrets import PASSWORD, TEST_EMAIL, RECIPIENT



def send_mail(guitars):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=TEST_EMAIL,
                            to_addrs=RECIPIENT,
                            msg = f"Subject: New Ibanez at Evenstad outlet\n\nThere are currently {len(guitars)} guitars at Evenstad's outlet page:\n"
                                  f"{guitars[0]}\n and {guitars[1]}")

    print(f"An email has been sent to {RECIPIENT}")
