import tkinter as tk

# Root window
root = tk.Tk()

# GUI Elements
bike_label = tk.Label(root, text="Enter amount of bikes:")
bike_entry = tk.Entry(root)

# Display elements
bike_label.grid(row=0, column=0)
bike_entry.grid(row=0, column=1)

# Main loop
root.mainloop()
