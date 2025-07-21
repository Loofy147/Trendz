from django.db import models
from django.db.models import F, Value, Case, When, ExpressionWrapper
from django.utils import timezone
from datetime import timedelta
from products.models import Product, Trend


class TrendingCalculator:
    @staticmethod
    def calculate_trending_scores():
        """Advanced trending algorithm considering multiple factors"""
        now = timezone.now()

        # Weight factors
        PRICE_WEIGHT = 0.3
        SEARCH_WEIGHT = 0.4

        trending_products = Product.objects.annotate(
            # Price volatility (higher = more trending)
            price_volatility=Case(
                When(
                    price_history__recorded_at__gte=now - timedelta(hours=24),
                    then=F("current_price") - F("price_history__price"),
                ),
                default=Value(0),
                output_field=models.DecimalField(),
            ),
            # Search volume growth
            search_growth=F("trend__search_volume") / Value(100.0),
            # Recency boost
            recency_factor=Case(
                When(created_at__gte=now - timedelta(days=7), then=Value(1.5)),
                When(created_at__gte=now - timedelta(days=30), then=Value(1.2)),
                default=Value(1.0),
            ),
            # Combined trending score
            calculated_score=models.ExpressionWrapper(
                (
                    F("price_volatility") * PRICE_WEIGHT
                    + F("search_growth") * SEARCH_WEIGHT
                )
                * F("recency_factor"),
                output_field=models.FloatField(),
            ),
        ).filter(calculated_score__gt=0)

        # Update trending scores
        for product in trending_products:
            Trend.objects.update_or_create(
                product=product, defaults={"trending_score": product.calculated_score}
            )
