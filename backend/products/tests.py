from django.test import TestCase
from .models import Product, Trend, PriceHistory
from .views import ProductViewSet


class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=10.00,
            source_url="https://example.com/product",
        )
        self.assertEqual(product.name, "Test Product")

    def test_get_trending_products(self):
        # Create some products and trends
        for i in range(25):
            product = Product.objects.create(
                name=f"Test Product {i}",
                description=f"This is test product {i}.",
                price=10.00 + i,
                source_url=f"https://example.com/product/{i}",
            )
            Trend.objects.create(
                product=product,
                trending_score=100 - i,
            )
            PriceHistory.objects.create(
                product=product,
                price=10.00 + i,
            )

        # Create a viewset and call the method
        viewset = ProductViewSet()
        with self.assertNumQueries(2):
            trending_products = viewset.get_trending_products()
            self.assertEqual(len(trending_products), 20)
