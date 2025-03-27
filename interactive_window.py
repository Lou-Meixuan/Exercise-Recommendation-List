import tkinter as tk
import data_loader

root = tk.Tk()
root.geometry('600x800')
    
label = tk.Label(root, text='Workout Wizard', font=("Courier", 30)).pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="white",
    fg="black",
).pack()

# Change the label text 
def show(): 
    label.config( text = clicked.get() ) 
  
# Dropdown menu options 
options = [ 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
] 
  
# datatype of menu text 
clicked = tk.StringVar() 
  
# initial menu text 
clicked.set( "Monday" ) 
  
# Create Dropdown menu 
drop = tk.OptionMenu(root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text 
button = tk.Button(root , text = "click Me" , command = show ).pack() 
  
# Create Label 
label = tk.Label(root , text = " " ) 
label.pack() 

# Start the GUI event loop
root.mainloop()
