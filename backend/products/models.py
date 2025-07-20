from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, default=0.00)
    description = models.TextField()
    source_url = models.URLField(unique=True, default='')
    last_scraped = models.DateTimeField(auto_now=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'price']),
            models.Index(fields=['last_scraped']),
        ]

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['product', 'date']),
        ]

class Trend(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='trend')
    score = models.FloatField(default=0.0)
    last_calculated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['score']),
        ]
