import pytest
from rest_framework.test import APIClient
from products.models import Product
from users.models import User
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
    """Create API client"""
    return APIClient()

@pytest.fixture
def test_user(db):
    """Create test user"""
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )

@pytest.fixture
def authenticated_client(api_client, test_user):
    """Create authenticated API client"""
    token = Token.objects.create(user=test_user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return api_client

@pytest.mark.django_db
def test_get_products(authenticated_client):
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
    response = authenticated_client.get('/api/v1/products/')
    assert response.status_code == 200
    assert len(response.data['results']) == 2

@pytest.mark.django_db
def test_get_product_detail(authenticated_client):
    product = Product.objects.create(
        name='Test Product',
        price=10.00,
        description='Test Description',
        source_url='http://example.com/product'
    )
    response = authenticated_client.get(f'/api/v1/products/{product.id}/')
    assert response.status_code == 200
    assert response.data['name'] == 'Test Product'
