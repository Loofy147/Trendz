from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_trending_products(self):
        cache_key = 'trending_products_v1'
        trending = cache.get(cache_key)

        if not trending:
            trending = Product.objects.select_related('trend').filter(
                trend__trending_score__gt=50
            ).order_by('-trend__trending_score')[:20]
            cache.set(cache_key, trending, 300)  # 5 minutes

        return trending

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_trending_products()
        return super().list(request, *args, **kwargs)
