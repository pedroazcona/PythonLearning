# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:39:19 2018

@author: poaa
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:28:27 2018

@author: poaa
"""

from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.configure(background='grey')
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.create_line(10, 10, 300, 50, fill='red', width=3)

root.mainloop()