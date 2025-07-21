from celery import shared_task
from .scraper import EnhancedScraper
import asyncio


@shared_task(bind=True, max_retries=3)
def scrape_products_async(self, source_urls):
    try:
        scraper = EnhancedScraper()
        return asyncio.run(scraper.scrape_multiple(source_urls))
    except Exception as exc:
        self.retry(countdown=60, exc=exc)
