import tkinter as tk

# Root window
root = tk.Tk()

# Option List
optionList = ['Hourly', 'Daily', 'Weekly']

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
rent_button = tk.Button(root, text='Rent')
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
