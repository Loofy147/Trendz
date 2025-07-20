from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product
from users.models import User
from rest_framework.authtoken.models import Token

class ProductAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_products(self):
        Product.objects.create(
            name='Test Product 1',
            price=10.00,
            description='Test Description 1',
            source_url='http://example.com/product1'
        )
        Product.objects.create(
            name='Test Product 2',
            price=20.00,
            description='Test Description 2',
            source_url='http://example.com/product2'
        )
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_product_detail(self):
        product = Product.objects.create(
            name='Test Product',
            price=10.00,
            description='Test Description',
            source_url='http://example.com/product'
        )
        response = self.client.get(f'/api/v1/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')
