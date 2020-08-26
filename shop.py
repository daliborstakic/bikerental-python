from datetime import datetime

class Shop:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"We currently have {self.stock} bike/s in stock.")
        return self.stock

    def rentBike(self, n_bikes=1, rentalBasis=1):
        now = datetime.now()
        return now, n_bikes, rentalBasis

    def issueBill(self, return_request):
        returnTime, num_of_bikes, rentalRate = return_request
        rentalTime = datetime.now - returnTime
        
        if return_request != None:
            if rentalRate == 1:
                bill = round(rentalTime.seconds / 3600) * 5 * num_of_bikes
            elif rentalRate == 2:
                bill = round(rentalTime.days) * 10 * num_of_bikes
            elif rentalTime == 3:
                bill = round(rentalTime.days / 7) * 30 * num_of_bikes
            
            if 3 <= num_of_bikes <= 5:
                bill *= 0.7
                return bill
            else:
                return bill

class Customer():
    def __init__(self):
        self.rentalBasis = 0
        self.n_bikes = 0

    def requestBike(self, rentalBasis=1, n_bikes=1):
        self.rentalBasis = rentalBasis
        self.n_bikes = n_bikes
        return self.rentalBasis, self.n_bikes
    