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

class ProductSerializer(serializers.ModelSerializer):
    price_history = PriceHistorySerializer(many=True, read_only=True)
    trend = TrendSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'source_url', 'last_scraped', 'created_at', 'updated_at', 'price_history', 'trend']
