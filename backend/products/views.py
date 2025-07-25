from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache


from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_trending_products(self):
        from django.utils import timezone
        from datetime import timedelta
        from .models import Trend, PriceHistory
        from django.db.models import Subquery, OuterRef

        cache_key = "trending_products_v1"
        trending = cache.get(cache_key)

        if not trending:
            yesterday = timezone.now() - timedelta(hours=24)

            # Subquery to get the latest price from yesterday
            latest_price_subquery = (
                PriceHistory.objects.filter(
                    product=OuterRef("pk"), recorded_at__gte=yesterday
                )
                .order_by("-recorded_at")
                .values("price")[:1]
            )

            trending = (
                Product.objects.select_related("trend")
                .filter(trend__trending_score__gt=50)
                .annotate(old_price=Subquery(latest_price_subquery))
                .order_by("-trend__trending_score")[:20]
            )

            trends_to_update = []
            for product in trending:
                if product.old_price:
                    product.trend.price_change_24h = float(
                        product.price - product.old_price
                    )
                else:
                    product.trend.price_change_24h = 0.0
                trends_to_update.append(product.trend)

            Trend.objects.bulk_update(trends_to_update, ["price_change_24h"])

            cache.set(cache_key, trending, 300)  # 5 minutes

        return trending

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_trending_products()
        return super().list(request, *args, **kwargs)
