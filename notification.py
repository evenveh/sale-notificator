import smtplib
from get_secrets import get_secret


def unwrap_product_string(products):
    product_string = "\n".join(products)
    return product_string


def sort_recipients_and_subscriptions(price_dict):
    """ Sorts and returns a list of unique subscribers from the price dictionary.
    :param price_dict: A dictionary containing products and related information, including subscribers.
    :return: a list of unique subscribers from the price_dict
    """
    subscribers = []
    for product, details in price_dict.items():
        for subscriber in details.get("subscribers", []):
            subscribers.append(subscriber)
    return list(set(subscribers))


def craft_message_for_updated_prices(price_dict, subscriber):
    price_lines = [f"{key}: {value['price']}" for key, value in price_dict.items() if
                   subscriber in value["subscribers"]]

    msg = "Subject: Price update\n\nHere are the prices:\n\n" + "\n".join(price_lines)

    return msg


def send_mail(message, subscriber):
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=get_secret("FROM_EMAIL"), password=get_secret("PASSWORD"))
            connection.sendmail(from_addr=get_secret("FROM_EMAIL"),
                                to_addrs=subscriber,
                                msg=message)

        print(f"An email has been sent to {get_secret("RECIPIENT")}")

    except Exception as e:
        print(f"Failed sending mail.\n Exception: {e}")
