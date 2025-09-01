from urllib.parse import urlparse

pages_and_keys = {
    'xxl.no': '[data-testid="selling-price"]',
    'bondekompaniet.no': 'span[itemprop="price"]'
}

url = "https://www.xxl.no/abc"
url = "https://bondekompaniet.no/norsk-naturgjodsel-helgjodsel-15-liter-98003951118"


def find_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain


def find_price_tag(url):
    domain = find_domain(url)
    if domain in pages_and_keys:
        return pages_and_keys[domain]
    else:
        return None


print(find_price_tag(url))
