import tkinter as tk
import time

window = tk.Tk()

canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

x = 0

def update_canvas():
    global x
    canvas.delete("all")
    canvas.create_oval(x, 50, x + 20, 70, fill="red")
    x += 1
    if x < 200:
        window.after(10, update_canvas)

update_canvas()

window.mainloop()
