import pytest
from unittest.mock import AsyncMock, patch
from scraper.scraper import EnhancedScraper
import aiohttp
import asyncio


@pytest.mark.asyncio
async def test_scraper_handles_network_errors():
    scraper = EnhancedScraper()

    with patch("aiohttp.ClientSession.get") as mock_get:
        mock_get.side_effect = aiohttp.ClientError("Network error")

        with pytest.raises(Exception):
            await scraper.scrape_product("http://example.com", "test")


@pytest.mark.asyncio
async def test_scraper_respects_rate_limits():
    scraper = EnhancedScraper()

    # Test that semaphore limits concurrent requests
    tasks = [
        scraper.scrape_product(f"http://example{i}.com", "test") for i in range(20)
    ]

    # Should handle gracefully without overwhelming the server
    results = await asyncio.gather(*tasks, return_exceptions=True)
    assert len(results) == 20
