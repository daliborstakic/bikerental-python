from datetime import datetime

class Shop:
    def __init__(self, stock=1):
        self.stock = stock if stock > 0 else 1 # Setting initial stock

    # Returning the stock parameter
    def display_stock(self):
        return self.stock

    # Renting the bike
    def rentBike(self, n_bikes=1):
        now = datetime.now() # Getting current time

        if n_bikes >= 1:
            self.stock -= n_bikes # Substracing the number of bikes rented
            return now
        else:
            raise ValueError # Returning an error for invalid value

    # Returning the bill
    def issueBill(self, return_request):
        rentalTime, num_of_bikes, rentalRate = return_request # Amount of time rented, bikes and rental rate
        
        if return_request != None:
            if rentalRate == 1: # If it's hourly
                bill = round(rentalTime.seconds / 3600) * 5 * num_of_bikes
            elif rentalRate == 2: # IF it's daily
                bill = round(rentalTime.days) * 10 * num_of_bikes
            elif rentalTime == 3: # If it's weekly
                bill = round(rentalTime.days / 7) * 30 * num_of_bikes
            
            if 3 <= num_of_bikes <= 5:
                bill *= 0.7 # Applying the discount

            self.stock += num_of_bikes # Same as the above
            return bill    


class Customer():
    def __init__(self): # These values get overridden anyway
        self.rentalBasis = 0
        self.n_bikes = 0

    # Sending an rent request
    # This function goes in motion with rentBike()
    def requestBike(self, rentalBasis=1, n_bikes=1):
        self.rentalBasis = rentalBasis
        self.n_bikes = n_bikes
        return self.rentalBasis, self.n_bikes # Returning the parameters
    
    # Customer returning bike
    def returnBike(self, when_rented):
        rented_time = datetime.now() - when_rented
        return rented_time, self.n_bikes, self.rentalBasis # Returns a request for issue_bill()
