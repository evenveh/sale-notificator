import unittest
from unittest.mock import patch
from sale_comparator import compare_sales

class TestCompareSales(unittest.TestCase):


    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_no_changes_in_sales(self, mock_unwrap, mock_send_mail):
        old_sales = ['Product A', 'Product B']
        current_sales = ['Product A', 'Product B']

        new_products, expired_products = compare_sales(old_products=old_sales, current_products = current_sales)
        self.assertEqual(new_products, [])
        self.assertEqual(expired_products, [])

    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_new_products_on_sale(self, mock_unwrap, mock_send_mail):
        old_sales = ['Product A']
        current_sales = ['Product A', 'Product B']
        new_products, expired_products = compare_sales(old_products = old_sales, current_products= current_sales)
        self.assertEqual(new_products, ['Product B'])
        self.assertEqual(expired_products, [])


    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_products_no_longer_on_sale(self, mock_unwrap, mock_send_mail):
        old_sales = ['Product A', 'Product B']
        current_sales = ['Product A']
        new_products, expired_products = compare_sales(old_products=old_sales, current_products= current_sales)
        self.assertEqual(new_products, [])
        self.assertEqual(expired_products, ['Product B'])



    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_both_new_and_expired_products(self, mock_unwrap, mock_send_mail):
        old_sales = ['Product A']
        current_sales = ['Product B']
        new_products, expired_products = compare_sales(old_products=old_sales, current_products= current_sales)
        self.assertEqual(new_products, ['Product B'])
        self.assertEqual(expired_products, ['Product A'])


if __name__ == '__main__':
    unittest.main()
