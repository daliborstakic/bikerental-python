import unittest
from datetime import datetime
from shop import Shop, Customer # Importing the shop module


class ShopTest(unittest.TestCase):
    # Initial instances for testing
    def setUp(self):
        self.shop1 = Shop()
        self.shop2 = Shop(10)
        self.shop3 = Shop(-1)

    # Checking if the stock returns correctly
    def test_display_stock(self):
        self.assertEqual(self.shop1.display_stock(), 1)
        self.assertEqual(self.shop2.display_stock(), 10)
        self.assertEqual(self.shop3.display_stock(), 1)

    # Checking if the stock can increase or decrease
    def test_stock_change(self):
        self.assertEqual(self.shop1.display_stock(), 1)
        self.shop1.rentBike()
        self.assertEqual(self.shop1.display_stock(), 0)
        self.assertEqual(self.shop2.display_stock(), 10)
        self.shop2.rentBike()
        self.assertEqual(self.shop2.display_stock(), 9)

    # Checking if the method returns correct values
    def test_rent_bike(self):
        now = datetime.now()
        self.assertEqual(self.shop1.rentBike(), (now, 1, 1))
        self.assertEqual(self.shop2.rentBike(2, 2), (now, 2, 2))
        with self.assertRaises(ValueError): # Context manager for checking a raise value
            self.shop3.rentBike(-1, 2)


if __name__ == '__main__':
    unittest.main()
