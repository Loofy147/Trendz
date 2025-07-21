from django.core.management.base import BaseCommand
from django.test.utils import override_settings
import time
from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Benchmark trending products query
        start = time.time()
        trending = list(
            Product.objects.select_related("trend").order_by("-trend__trending_score")[
                :100
            ]
        )
        query_time = time.time() - start

        self.stdout.write(
            f"Trending query: {query_time:.3f}s for {len(trending)} products"
        )

        # Benchmark API response time
        from django.test import Client

        client = Client()

        start = time.time()
        client.get("/api/v1/products/?page_size=50")
        api_time = time.time() - start

        self.stdout.write(f"API response: {api_time:.3f}s")
