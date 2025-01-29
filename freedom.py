from datetime import date, timedelta
import datetime

# Create two date objects
#date1 = date(2025, 1, 20)
date1 = datetime.date.today()
date2 = date(2029, 1, 20)

# Calculate the difference between two dates
delta = date2 - date1 
print(delta.days)

#import tkinter as tk
#
#root = tk.Tk()
#root.title("Place Example")
#
## Create a label
#label = tk.Label(root, text=delta.days)
#
## Place the label at specific coordinates
#label.place(x=50, y=50)

#root.mainloop()

from tkinter import *

main = Tk()
ourMessage = 'This is our Message'
messageVar = Message(main, text=delta.days)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()


