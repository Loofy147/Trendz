import pytest
from unittest.mock import patch, AsyncMock
from scraper.scraper import EnhancedScraper

@pytest.mark.asyncio
async def test_scrape_product():
    with patch('aiohttp.ClientSession') as mock_session:
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.text.return_value = """
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
        """
        mock_session.get.return_value.__aenter__.return_value = mock_response

        scraper = EnhancedScraper()
        scraper.session = mock_session

        with patch('products.models.Product.objects.aupdate_or_create', new_callable=AsyncMock) as mock_update_or_create:
            mock_update_or_create.return_value = (None, None)
            with patch('products.models.PriceHistory.objects.acreate', new_callable=AsyncMock) as mock_create:
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
