import unittest
from unittest.mock import patch
from sale_comparator import compare_sales, create_message

class TestCompareSales(unittest.TestCase):

    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_create_message_with_new_and_expired_products(self, mock_unwrap, mock_send_mail):
        mock_unwrap.side_effect = lambda products: '\n'.join(products)
        new_products = ['Product A']
        old_products = ['Product B']
        current_products = ['Product A', 'Product B']
        url = "https://example.com"

        create_message(new_products, old_products, current_products, url)

        expected_message = (
            "Subject: Update on sales\n\n There are both new and expired products.\n\n"
            " New products: Product A\n\n Expired products:Product B \n\nURL: https://example.com"
        )
        self.once_with = mock_send_mail.assert_called_once_with(message=expected_message)

    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_create_message_with_only_new_products(self, mock_unwrap, mock_send_mail):
        mock_unwrap.side_effect = lambda products: '\n'.join(products)
        new_products = ['Product A']
        old_products = []
        current_products = ['Product A', 'Product C']
        url = "https://example.com"

        create_message(new_products, old_products, current_products, url)

        expected_message = (
            "Subject: New Ibanez guitar at Evenstad Outlet\n\n"
            "There is a new product on Evenstad's outlet page: Product A. \n"
            " There are currently 2 guitars out: \n\nProduct A\nProduct C\n\n URL: https://example.com"
        )
        mock_send_mail.assert_called_once_with(message=expected_message)


    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_message_with_only_expired_products(self, mock_unwrap, mock_send_mail):
        mock_unwrap.side_effect = lambda products: '\n'.join(products)
        new_products = []
        old_products = ['Product B']
        current_products = ['Product A']
        url = "https://example.com"

        create_message(new_products, old_products, current_products, url)

        expected_message = (
            "Subject: Product no longer for sale at Evenstad's Outlet\n\n"
            " The product: Product B is no longer for sale. \n"
            " There are currently 1 guitars out: \n\nProduct A\n\n URL: https://example.com"
        )
        mock_send_mail.assert_called_once_with(message=expected_message)

    @patch('sale_comparator.send_mail')
    @patch('sale_comparator.unwrap_product_string')
    def test_message_with_no_changes(self, mock_unwrap, mock_send_mail):
        new_products = []
        old_products = []
        current_products = ['Product A']
        url = "https://example.com"

        create_message(new_products, old_products, current_products, url)

        mock_send_mail.assert_not_called()

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
