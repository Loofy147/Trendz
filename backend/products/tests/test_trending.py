import pytest
from django.utils import timezone
from datetime import timedelta
from products.models import Product, Trend, PriceHistory
from products.utils.trending import TrendingCalculator


@pytest.mark.django_db
def test_calculate_trending_scores():
    # Create a product
    product = Product.objects.create(
        name="Test Product",
        price=100.00,
        current_price=100.00,
        created_at=timezone.now() - timedelta(days=5),
    )

    # Create price history
    PriceHistory.objects.create(
        product=product, price=90.00, recorded_at=timezone.now() - timedelta(hours=12)
    )

    # Create a trend for the product
    Trend.objects.create(product=product, search_volume=500)

    # Calculate trending scores
    TrendingCalculator.calculate_trending_scores()

    # Refresh the trend from the database
    trend = Trend.objects.get(product=product)

    # Assert that the trending score has been updated
    assert trend.trending_score > 0
