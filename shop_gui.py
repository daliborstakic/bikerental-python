import tkinter as tk
from shop import Shop, Customer

# Root window
root = tk.Tk()

# Option List
optionList = ['Hourly', 'Daily', 'Weekly']

# Shop and Customer variables
customer = Customer()
shop = Shop(stock=10)
global when_rented

# Switch-like method for getting OptionMenu index
def get_list_index(argument):
    switcher = {
        'Hourly': 1,
        "Daily": 2,
        "Weekly": 3,
    }
    return switcher.get(argument)

# return_bike functionality
def rent_bike():
    global when_rented

    if bike_entry.get() == "":
        set_status("Cannot be empty!", "red") # In empty, show status
    else:
        try:
            num_of_bikes = int(bike_entry.get()) # If it's not a number
        except ValueError:
            set_status("Enter a number!", "red") # Shows a warning

        # Button state
        if rent_button['state'] == tk.NORMAL:
            rent_button['state'] = tk.DISABLED
        
        if return_button['state'] == tk.DISABLED:
            return_button['state'] = tk.NORMAL

        # Using the get_list_index method
        rental_basis = get_list_index(variable.get())
        
        # Renting the actual bike
        customer.requestBike(rental_basis, num_of_bikes)
        when_rented = shop.rentBike(customer.num_of_bikes)

        # Update stock label
        display_stock()

def return_bike():
    return_request = customer.returnBike(when_rented)
    bill = shop.issueBill(return_request)

    # Returns the bill
    set_status(f"You bill is {bill}", "green")

    # Button state
    if return_button['state'] == tk.NORMAL:
        return_button['state'] = tk.DISABLED

    if rent_button['state'] == tk.DISABLED:
        rent_button['state'] = tk.NORMAL
    
    display_stock()

def set_status(message, color="black"):
    status = tk.Label(root, text=message, fg=color)
    status.grid(row=2, column=0)

def display_stock():# Stock display
    stock_label = tk.Label(root, text=f"The current shop stock is {shop.stock}")
    stock_label.grid(row=4, column=0)

# Tkinter variable
variable = tk.StringVar(root)
variable.set(optionList[0])

# First row
bike_label = tk.Label(root, text="Enter amount of bikes:")
bike_entry = tk.Entry(root)

# Second row
rental_label = tk.Label(root, text="Choose rental basis:")
rental_list = tk.OptionMenu(root, variable, *optionList)

# Third row*
rent_button = tk.Button(root, text='Rent', command=rent_bike)
return_button = tk.Button(root, text='Return', command=return_bike, state=tk.DISABLED)

# Display elements
bike_label.grid(row=0, column=0)
bike_entry.grid(row=0, column=1)

rental_label.grid(row=1, column=0)
rental_list.grid(row=1, column=1)

# *It's the fourth row because a label will be inserted later at
# the actual third row
rent_button.grid(row=3, column=0)
return_button.grid(row=3, column=1)

# Stock display
display_stock()

# Main loop
root.mainloop()
