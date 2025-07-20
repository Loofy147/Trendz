import requests
from bs4 import BeautifulSoup
from products.models import Product

def scrape_products():
    url = 'https://fake-ecommerce.com/products'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for product_div in soup.find_all('div', class_='product'):
        name = product_div.find('h2').text
        description = product_div.find('p', class_='description').text
        price = float(product_div.find('span', class_='price').text.replace('$', ''))
        image_url = product_div.find('img')['src']
        product_url = product_div.find('a')['href']

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            image_url=image_url,
            url=product_url,
        )
