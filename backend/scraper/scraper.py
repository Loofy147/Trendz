import asyncio
import aiohttp
from bs4 import BeautifulSoup
from products.models import Product, PriceHistory
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

logger = logging.getLogger(__name__)


class EnhancedScraper:
    def __init__(self):
        self.session = None
        self.semaphore = asyncio.Semaphore(10)  # Max 10 concurrent requests

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    async def scrape_product(self, url, source_name):
        async with self.semaphore:  # Rate limiting
            try:
                async with self.session.get(url, timeout=30) as response:
                    if response.status == 200:
                        content = await response.text()
                        data = await self.parse_product(content)
                        await self.save_product(data, source_name)
                        return data
            except asyncio.TimeoutError:
                logger.warning(f"Timeout scraping {url}")
                raise
            except Exception as e:
                logger.error(f"Error scraping {url}: {e}")
                raise

    async def parse_product(self, content):
        soup = BeautifulSoup(content, "html.parser")
        name = soup.find("h2").text
        description = soup.find("p", class_="description").text
        price = float(soup.find("span", class_="price").text.replace("$", ""))
        source_url = soup.find("a")["href"]
        return {
            "name": name,
            "description": description,
            "price": price,
            "source_url": source_url,
        }

    async def save_product(self, product_data, source):
        product, created = await Product.objects.aupdate_or_create(
            source_url=product_data["source_url"],
            defaults={
                "name": product_data["name"],
                "description": product_data["description"],
                "price": product_data["price"],
            },
        )

        await PriceHistory.objects.acreate(
            product=product, price=product_data["price"], source=source
        )

    async def scrape_multiple(self, urls):
        async with self:
            tasks = [self.scrape_product(url, "batch_source") for url in urls]
            return await asyncio.gather(*tasks)


async def main():
    async with EnhancedScraper() as scraper:
        await scraper.scrape_product(
            "https://fake-ecommerce.com/products", "fake-ecommerce"
        )


if __name__ == "__main__":
    asyncio.run(main())
