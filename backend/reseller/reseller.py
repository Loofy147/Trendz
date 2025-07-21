from products.models import Product
from sales.models import Sale


def identify_trending_products():
    trending_products = []
    for product in Product.objects.all():
        sales_count = Sale.objects.filter(product=product).count()
        if sales_count > 10:  # Identify products with more than 10 sales as trending
            trending_products.append(product)
    return trending_products


def resell_trending_products():
    trending_products = identify_trending_products()
    for product in trending_products:
        # Automate the process of purchasing and relisting the product
        print(f"Reselling {product.name}...")
