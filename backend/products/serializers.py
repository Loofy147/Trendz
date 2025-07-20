from rest_framework import serializers
from .models import Product, PriceHistory, Trend

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = '__all__'

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = '__all__'

from django.utils import timezone
from datetime import timedelta

class ProductSerializer(serializers.ModelSerializer):
    price_history = PriceHistorySerializer(many=True, read_only=True)
    trend = TrendSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'source_url', 'last_scraped', 'created_at', 'updated_at', 'price_history', 'trend']

class ProductDetailSerializer(serializers.ModelSerializer):
    price_history = PriceHistorySerializer(many=True, read_only=True)
    trending_data = TrendSerializer(source='trend', read_only=True)
    price_change_24h = serializers.SerializerMethodField()

    def get_price_change_24h(self, obj):
        # Calculate 24h price change
        yesterday = timezone.now() - timedelta(hours=24)
        try:
            old_price = obj.price_history.filter(
                recorded_at__gte=yesterday
            ).first().price
            return float(obj.price - old_price)
        except AttributeError:
            return 0.0

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'source_url', 'last_scraped', 'created_at', 'updated_at', 'price_history', 'trending_data', 'price_change_24h']
