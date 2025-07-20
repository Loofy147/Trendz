import pytest
from unittest.mock import patch, AsyncMock
from scraper.scraper import EnhancedScraper
from aioresponses import aioresponses

@pytest.mark.asyncio
async def test_scrape_product():
    with aioresponses() as m:
        m.get('http://example.com', status=200, body="""
        <html>
            <body>
                <div class="product">
                    <h2>Test Product</h2>
                    <p class="description">Test Description</p>
                    <span class="price">$10.00</span>
                    <a href="http://example.com/product"></a>
                </div>
            </body>
        </html>
        """)

        with patch('products.models.Product.objects.aupdate_or_create', new_callable=AsyncMock) as mock_update_or_create:
            mock_update_or_create.return_value = (None, None)
            with patch('products.models.PriceHistory.objects.acreate', new_callable=AsyncMock) as mock_create:
                async with EnhancedScraper() as scraper:
                    await scraper.scrape_product('http://example.com', 'test')

                mock_update_or_create.assert_called_once_with(
                    source_url='http://example.com/product',
                    defaults={
                        'name': 'Test Product',
                        'description': 'Test Description',
                        'price': 10.0,
                    }
                )
                mock_create.assert_called_once()
