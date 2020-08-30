import tkinter as tk

# Root window
root = tk.Tk()

# Option List
optionList = ['Hourly', 'Daily', 'Weekly']

def get_list_index(argument):
    switcher = {
        'Hourly': 1,
        "Daily": 2,
        "Weekly": 3,
    }
    return switcher.get(argument)

# return_bike functionality
def rent_bike():
    if bike_entry.get() == "":
        set_status("Cannot be empty!", "red") # In empty, show status
    else:
        try:
            num_of_bikes = int(bike_entry.get())
        except ValueError:
            set_status("Enter a number!", "red")

        rental_basis = get_list_index(variable.get())

def set_status(message, color="black"):
    status = tk.Label(root, text=message, fg=color)
    status.grid(row=2, column=0)

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
return_button = tk.Button(root, text='Return', state=tk.DISABLED)

# Display elements
bike_label.grid(row=0, column=0)
bike_entry.grid(row=0, column=1)

rental_label.grid(row=1, column=0)
rental_list.grid(row=1, column=1)

# *It's the fourth row because a label will be inserted later at
# the actual third row
rent_button.grid(row=3, column=0)
return_button.grid(row=3, column=1)

# Main loop
root.mainloop()
