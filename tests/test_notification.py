import unittest
from notification import unwrap_product_string

class TestUnwrapProductString(unittest.TestCase):

    def test_unwrap_product_string(self):
        products = ['Product A', 'Product B', 'Product C']
        expected_result = 'Product A\nProduct B\nProduct C'
        result = unwrap_product_string(products)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
