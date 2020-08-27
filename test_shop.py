import unittest
from datetime import datetime, timedelta
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
        # The test kept failing because the miliseconds are not equal
        # But they are mostly a few miliseconds apart
        self.assertEqual(self.shop1.rentBike(), datetime.now())
        self.assertEqual(self.shop2.rentBike(2), datetime.now())

        with self.assertRaises(ValueError): # Context manager checking for a raise value
            self.shop3.rentBike(-1)

    # Testing the issue_bill() method
    def test_issue_bill(self):
        self.assertIsNone(self.shop1.issueBill()) # Checking if return_request is None
        
        with self.assertRaises(ValueError): # If the rental is not (1, 2, 3)
            self.shop1.issueBill((timedelta(), 1, 4))

        # Checking for the bill return value
        self.assertEqual(self.shop2.issueBill((timedelta(hours=2), 2, 1)), 20)
        self.assertEqual(self.shop2.issueBill((timedelta(days=3), 1, 2)), 30)
        self.assertEqual(self.shop2.issueBill((timedelta(weeks=2), 3, 3)), 126)

        # Checking if the bikes are returned
        self.shop3.rentBike()
        self.assertEqual(self.shop3.display_stock(), 0)
        self.shop3.issueBill((timedelta(), 1, 1))
        self.assertEqual(self.shop3.display_stock(), 1)


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.cust1 = Customer()
        self.cust2 = Customer()


# Main running
if __name__ == '__main__':
    unittest.main()
