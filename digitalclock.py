'''Debargha Bhattacharjee NSEC CSE First year'''


# Modules
from tkinter import * #module used to make gui projects
from time import strftime #module to import time from the system 

r = Tk()  # Creates tkinter window, tk() is a class
r.title("Digital Computer Clock")  # Adds title

# Function for the format of the clock
def time():
    string = strftime("%H:%M:%S %p")
    l.config(text = string)
    l.after(1000, time)

# Configuring the layout
l = Label(r, font = ("arial", 160, "bold"),bg="black",fg="white")

# Packs widgets(the gui) into rows or columns and positions label
l.pack(anchor = "center",fill = "both",expand=1)

time()  # Time function 

mainloop()   # used as the application program
