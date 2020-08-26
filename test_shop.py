import unittest
from shop import Shop, Customer


class ShopTest(unittest.TestCase):
    def setUp(self):
        self.shop1 = Shop()
        self.shop2 = Shop(10)

    def test_display_stock(self):
        self.assertEqual(self.shop1.display_stock(), 0)
        self.assertEqual(self.shop2.display_stock(), 10)


if __name__ == '__main__':
    unittest.main()
