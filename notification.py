import smtplib
from get_secrets import get_secret
from time import sleep


def find_all_subscribers(price_dict):
    """
    Sorts and returns a list of unique subscribers from the price dictionary.
    :param price_dict: A dictionary containing products as keys and dictionaries as values. Each of these
    dictionaries have information related to the product, subscribers being one of their values.
    :return: a list of all subscribers found in price_dict without duplicates.
    """
    subscribers = []
    for product, details in price_dict.items():
        for subscriber in details.get("subscribers", []):
            subscribers.append(subscriber)
    return list(set(subscribers))


def craft_message_for_updated_prices(price_dict, subscriber):
    """
    Crafts an email message for a subscriber based on updated product prices.

    This function checks the `price_dict` for products subscribed to by the given `subscriber`.
    If the product's price is below the subscriber's threshold, it includes the product in the email message.

    :param price_dict: A dictionary containing product details. Each key is a product name, and the value is a dictionary
                       with keys such as 'price', 'subscribers', and 'threshold'.
    :param subscriber: The email address of the subscriber to whom the message is being crafted.
    :return: A formatted email message string if there are products below the threshold; otherwise, None.
    """
    price_lines = [f"{key}: {value['price']}" for key, value in price_dict.items() if
                   subscriber in value["subscribers"]
                   and value["price"] < value["threshold"]]
    if price_lines:
        msg = ("Subject: Price update\n\nThe following products are announced to a lower price your desired threshold "
               "you have decided:\n\n") + "\n".join(price_lines)
        return msg
    return None


def send_mail_to_subscibers(subscribers, price_dict):
    """
        Sends email notifications to a list of subscribers about updated product prices.

        This function iterates through the list of subscribers and crafts a message for each subscriber
        based on the `price_dict`. If a message is successfully crafted, it sends the email using the `send_mail` function.
        A delay is added between sending emails.

        :param subscribers: A list of email addresses of all subscribers contained in price_dict.
        :param price_dict: A dictionary containing product details. Each key is a product name, and the value is a dictionary
                           with keys such as 'price', 'subscribers', and 'threshold'.
        """
    for subscriber in subscribers:
        message = craft_message_for_updated_prices(price_dict, subscriber)
        if message:
            send_mail(message, subscriber)
        sleep(10)


def send_mail(message, receiver):
    """
    Sends an email to a specified receiver (email address) with a given message.

    This function uses the SMTP protocol to send an email. It retrieves the sender's email and password
    from secrets using the `get_secret` function. The email is sent to the specified subscriber with the
    provided message. If the email fails to send, an exception is caught and logged.

    :param message: The email message to be sent. This should include the subject and body of the email.
    :param receiver: The recipient's email address.
    """
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=get_secret("FROM_EMAIL"), password=get_secret("PASSWORD"))
            connection.sendmail(from_addr=get_secret("FROM_EMAIL"),
                                to_addrs=receiver,
                                msg=message)

        print(f"An email has been sent to {receiver} with the following message:\n{message}")

    except Exception as e:
        print(f"Failed sending mail.\n Exception: {e}")
