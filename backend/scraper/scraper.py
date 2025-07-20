import requests
from bs4 import BeautifulSoup
from products.models import Product
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def scrape_products():
    url = 'https://fake-ecommerce.com/products'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    for product_div in soup.find_all('div', class_='product'):
        name = product_div.find('h2').text
        description = product_div.find('p', class_='description').text
        price = float(product_div.find('span', class_='price').text.replace('$', ''))
        source_url = product_div.find('a')['href']

        Product.objects.update_or_create(
            source_url=source_url,
            defaults={
                'name': name,
                'description': description,
                'price': price,
            }
        )
