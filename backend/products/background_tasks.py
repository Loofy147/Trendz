from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import PriceHistory, Product
from django.db.models import F, Q


@shared_task
def monitor_price_changes():
    """Monitor significant price changes and notify clients"""
    channel_layer = get_channel_layer()

    # Find products with >10% price change in last hour
    significant_changes = (
        PriceHistory.objects.filter(
            recorded_at__gte=timezone.now() - timedelta(hours=1)
        )
        .annotate(
            price_change_pct=(F("price") - F("product__current_price"))
            / F("product__current_price")
            * 100
        )
        .filter(Q(price_change_pct__gte=10) | Q(price_change_pct__lte=-10))
    )

    for change in significant_changes:
        async_to_sync(channel_layer.group_send)(
            "price_updates",
            {
                "type": "price_update",
                "product_id": change.product.id,
                "new_price": str(change.price),
                "change": change.price_change_pct,
            },
        )
