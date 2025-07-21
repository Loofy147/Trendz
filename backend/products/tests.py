from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=10.00,
            source_url="https://example.com/product",
        )
        self.assertEqual(product.name, "Test Product")
