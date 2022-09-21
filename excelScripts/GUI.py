import tkinter as tk
from tkinter import *
import datetime as dt
datetime_obj = dt.datetime.now()
title = ""


def label_add(frame, text, position):
    label = tk.Label(
        frame,
        text=text,
        font=('Arial', 12),
        width=100,
        height=50,
        anchor=position
    )
    label.pack()


# Creating window object
window = tk.Tk()
# Setting window title
window.title(title)

# topFrame = Frame(height=50)
# label_add(topFrame, "Patriot Technologies Inc. ", 'nw')


window.mainloop()
