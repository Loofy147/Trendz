from django.core.management.base import BaseCommand
from products.utils.trending import TrendingCalculator


class Command(BaseCommand):
    help = "Calculates and updates trending scores for products."

    def handle(self, *args, **options):
        self.stdout.write("Calculating trending scores...")
        TrendingCalculator.calculate_trending_scores()
        self.stdout.write(self.style.SUCCESS("Successfully updated trending scores."))
