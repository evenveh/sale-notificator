import unittest
from unittest.mock import patch, MagicMock
from sale_finder import PageScraper


class TestGetSales(unittest.TestCase):

    @patch("sale_finder.webdriver.Chrome")
    def test_find_products_on_page(self, mock_webdriver):
        mock_driver = MagicMock()
        mock_webdriver.return_value.__enter__.return_value = mock_driver

        mock_driver.find_elements.return_value = [
            MagicMock(
                find_element=MagicMock(
                    side_effect=lambda by, name: MagicMock(
                        text="Gibson Les Paul" if "AddHeader1" in name else "20% off")
                )
            )
        ]

        url = "https://www.example.com"
        page_scraper = PageScraper()
        result = page_scraper.find_products_on_page(url)

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Gibson Les Paul: 20% off", result)


if __name__ == "__main__":
    unittest.main()
