# Requirements
The main flow of the program:

1. Updates prices for all products in price_dict.
2. Finds all subscribers in price_dict.
3. Sends email notifications to subscribers if prices are lower than threshold.

The program is designed to be ran periodically, e.g., via a cron job, to check for price updates and notify subscribers accordingly.

price_dict is a dictionary based on a csv called product overview, containing product and subscriber data.
product_overview.csv would look something like this:


| Product Name | URL                          | Subscribers                                   | Price | Threshold |
|-------------|------------------------------|-----------------------------------------------|-------|-----------|
| Offroad Bike| https://examplewebpage1.com/ | examplemail1@gmail.com                        | 1.0   | 8000.0    |
| Samsung S25 | https://examplewebpage2.com/ | examplemail1@gmail.com, examplemail2@gmail.com, ... | 1.0   | 160.0     |
| Seagate 2TB| https://examplewebpage2.com/ | examplemail1@gmail.com, examplemail2@gmail.com, ... | 1.0   | 165.0     |

1. The product name can be anything, as it is just for reference. 
2. The URL is the URL to the product page.
3. Subscribers is a comma-separated list of email addresses to notify if the price drops below the threshold.
4. Price. This column is used by the program to store and compare the last known price with the threshold.
5. Threshold is the limit to which the price must drop to trigger a notification.


  
In order for a page to be scraped, the program must know what css selector to use to find the price on the page. 
This is configured in a separate csv called page_configuration.csv, which would look something like this:

| Domain                       | Key                                                                                                                          |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| https://examplewebpage1.com/ | [data-testid="selling-price"]                                                                                                |
| https://examplewebpage2.com/ | span[itemprop="price"]                                                                                                       |


1. The domain is the base URL of the website.
2. The key is the css selector used to find the price on the product page.

## Secrets
An email used to send notifications must be configured. The email is stored in a text file called FROM_EMAIL.txt,
which only contains the email in written words. Then there is a file called PASSWORD.txt, which contains the password for that email account.
These values are stored locally in a folder called secrets, stored in the root directory of the project.
