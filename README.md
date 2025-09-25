README will be updated with time. 
For now:

  The main flow of the program:
    1. Updates prices for all products in price_dict.
    2. Finds all subscribers in price_dict.
    3. Sends email notifications to subscribers if prices are lower than threshold.

where price_dict is a dictionary create based on a csv called product overview, containing product and subscriber data.
Such csv would look something like:


| Product Name          | URL                                | Subscribers                                   | Price | Threshold |
|-----------------------|------------------------------------|-----------------------------------------------|-------|-----------|
| Offroad Bike 2000     | [link](https://whereveryoubuybikes.com/) | examplemail1@gmail.com                        | 1.0   | 8000.0    |
| Samsung S25 Ultra     | [link](https://mobilesandelectronics.com/) | examplemail1@gmail.com, examplemail2@gmail.com, ... | 1.0   | 160.0     |
| Seagate 2TB hard drive| [link](https://mobilesandelectronics.com/) | examplemail1@gmail.com, examplemail2@gmail.com, ... | 1.0   | 165.0     |

1. The product name can be anything, as it is just for reference. 
2. The URL is the URL to the product page.
3. Subscribers is a comma-separated list of email addresses to notify if the price drops below the threshold.
4. Price. This column is used by the program to store and compare the last known price with the threshold.
5. Threshold is the limit to which the price must drop to trigger a notification.

  The program is designed to be run periodically, e.g., via a cron job, to check for price updates and notify subscribers accordingly.