import pytest
from products.models import Product, PriceHistory, Trend

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name='Test Product',
        price=10.00,
        description='Test Description',
        source_url='http://example.com/product'
    )
    assert product.name == 'Test Product'
    assert product.price == 10.00
    assert product.description == 'Test Description'
    assert product.source_url == 'http://example.com/product'

@pytest.mark.django_db
def test_price_history_creation():
    product = Product.objects.create(
        name='Test Product',
        price=10.00,
        description='Test Description',
        source_url='http://example.com/product'
    )
    price_history = PriceHistory.objects.create(
        product=product,
        price=10.00,
        source='test'
    )
    assert price_history.product == product
    assert price_history.price == 10.00
    assert price_history.source == 'test'

@pytest.mark.django_db
def test_trend_creation():
    product = Product.objects.create(
        name='Test Product',
        price=10.00,
        description='Test Description',
        source_url='http://example.com/product'
    )
    trend = Trend.objects.create(
        product=product,
        trending_score=0.5,
        price_velocity=0.1,
        search_volume=100
    )
    assert trend.product == product
    assert trend.trending_score == 0.5
    assert trend.price_velocity == 0.1
    assert trend.search_volume == 100
