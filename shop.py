from datetime import datetime

class Shop:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"We currently have {self.stock} bike/s in stock.")
        return self.stock
        