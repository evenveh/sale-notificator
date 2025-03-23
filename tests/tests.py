import unittest
from unittest.mock import patch

class TestCompareSales(unittest.TestCase):

    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_no_changes_in_sales(self, mock_unwrap, mock_send_mail):
        old_products = ['Product A', 'Product B']
        new_products = ['Product A', 'Product B']
        url = 'http://example.com'


    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_new_products_on_sale(self, mock_unwrap, mock_send_mail):
        old_products = ['Product A']
        new_products = ['Product A', 'Product B']
        url = 'http://example.com'

        mock_unwrap.return_value = 'Product A, Product B'


    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_products_no_longer_on_sale(self, mock_unwrap, mock_send_mail):
        old_products = ['Product A', 'Product B']
        new_products = ['Product A']
        url = 'http://example.com'

        mock_unwrap.return_value = 'Product A'


    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_both_new_and_expired_products(self, mock_unwrap, mock_send_mail):
        old_products = ['Product A']
        new_products = ['Product B']
        url = 'http://example.com'

        mock_unwrap.side_effect = ['Product B', 'Product A']


if __name__ == '__main__':
    unittest.main()