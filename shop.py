from datetime import datetime


class Shop:
    def __init__(self, stock=1):
        self.stock = stock if stock > 0 else 1 # Setting initial stock

    # Returning the stock parameter
    @property
    def display_stock(self):
        return self.stock

    @display_stock.setter
    def set_stock(self, value):
        self.set_stock = value

    # Renting the bike
    def rentBike(self, n_bikes=1):
        now = datetime.now() # Getting current time

        if n_bikes >= 1:
            new_stock = self.display_stock - n_bikes # Substracing the number of bikes rented
            self.set_stock(new_stock) # New stock
            return now
        else:
            raise ValueError # Returning an error for invalid value

    # Returning the bill
    def issueBill(self, return_request=None):
        if return_request != None:
            rentalTime, num_of_bikes, rentalRate = return_request # Amount of time rented, bikes and rental rate

            if rentalRate == 1: # If it's hourly
                bill = round(rentalTime.seconds / 3600) * 5 * num_of_bikes
            elif rentalRate == 2: # IF it's daily
                bill = round(rentalTime.days) * 10 * num_of_bikes
            elif rentalRate == 3: # If it's weekly
                bill = round(rentalTime.days / 7) * 30 * num_of_bikes
            else:
                raise ValueError

            if num_of_bikes >= 3:
                bill *= 0.7 # Applying the discount

            self.stock += num_of_bikes # Same as the above
            return round(bill)
        else:
            return None


class Customer():
    def __init__(self): # These values get overridden anyway
        self.rentalBasis = 0
        self.rented_bikes = 0

    # Sending an rent request
    # This function goes in motion with rentBike()
    def requestBike(self, rentalBasis=1, n_bikes=1):
        if 1 <= rentalBasis <= 3 and n_bikes >= 1:
            self.rentalBasis = rentalBasis
            self.rented_bikes = n_bikes
            return self.rentalBasis, self.rented_bikes # Returning the parameters
        else:
            raise ValueError
    
    @property
    def num_of_bikes(self):
        return self.rented_bikes
        
    @property
    def rental_basis(self):
        return self.rental_basis
    
    # Customer returning bike
    def returnBike(self, when_rented=None):
        if when_rented != None:
            rented_time = datetime.now() - when_rented
            return rented_time, self.rented_bikes, self.rentalBasis # Returns a request for issue_bill()
        else:
            return None
