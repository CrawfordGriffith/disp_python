import tkinter as tk

from PIL import Image, ImageFont, ImageDraw, ImageTk

from datetime import date, timedelta, datetime
#import datetime

# Create main window
window = tk.Tk()

# size the screen
horizontal = 1500
vertical = 750

# Make a canvas and get a drawing context to it
canvas = tk.Canvas(window, width=horizontal, height=vertical)
canvas.pack()

# Get a "Arial" TTF
arial_font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",95)

# Get a "Helvetica" TTF
impact_font = ImageFont.truetype("C:/Windows/Fonts/Impact.ttf",450)

# max the window
window.state('zoomed')

def update_display():
    global image, photo
    # window, draw, label, tk 
    
    text = datetime.now()
    window.title(text)

    delta = date(2029, 1, 20) - date.today()

    # remove items from canvas
    canvas.delete("all")
    import random

    image = Image.new(mode='RGB', size=(horizontal, vertical), color=(255,0,0))
    draw = ImageDraw.Draw(image)

    # Generate a random integer between 1 and 10 (both inclusive)
    random_red = random.randint(0, 127)
    print(random_red)
    random_grn = random.randint(0, 127)
    print(random_grn)
    random_blu = random.randint(0, 127)
    print(random_blu)


    draw.text((220,0),str(delta.days),font=impact_font, fill=(random_red,random_grn,random_blu))
    draw.text((20,500),"Days Until Democracy Returns",font=arial_font, fill=(0,255,255))
    # Convert the image to a PhotoImage for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Add the image to the canvas
    canvas.create_image(0, 0, anchor="nw", image=photo)

    window.after(5000, update_display)
                 
update_display()  # Start the periodic event


# Start the main event loop
window.mainloop()

