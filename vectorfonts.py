import tkinter as tk
from PIL import Image, ImageFont, ImageDraw

# Make a red canvas and get a drawing context to it
img = Image.new(mode='RGB', size=(500, 200), color=(255,0,0))
draw = ImageDraw.Draw(img)

# Get a "Chalkduster" TTF
chalk = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",16)

# Get a "Keyboard" TTF
kbd = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",26)

# Make example for Lazy One - showing how to colour cyan too
draw.text((40,40),"Keyboard",font=kbd, fill=(0,255,255))

# And another
draw.text((20,140),"Chalkduster",font=chalk)

# Convert the image to a PhotoImage for Tkinter
photo = tk.PhotoImage(img)
canvas.create_image(0, 0, anchor="nw", image=photo)

root.mainloop()
