from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, db_index=True, default=0.00
    )
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    source_url = models.URLField(unique=True, default="")
    last_scraped = models.DateTimeField(auto_now=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["name", "price"]),
            models.Index(fields=["last_scraped"]),
        ]


class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="price_history", db_index=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True, db_index=True)
    source = models.CharField(max_length=100, default="unknown")  # Track which site

    class Meta:
        ordering = ["-recorded_at"]
        indexes = [
            models.Index(fields=["product", "-recorded_at"]),
            models.Index(fields=["recorded_at"]),  # For time-based queries
        ]


class Trend(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="trend"
    )
    trending_score = models.FloatField(default=0.0, db_index=True)
    price_velocity = models.FloatField(default=0.0)  # Price change rate
    search_volume = models.IntegerField(default=0)
    price_change_24h = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-trending_score"]
