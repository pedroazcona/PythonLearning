# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:28:27 2018

@author: poaa
"""

from tkinter import *
from tkinter import ttk, font

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
#frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)

n = ttk.Notebook(content)
f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page
n.add(f1, text='One')
n.add(f2, text='Two')

p = ttk.Panedwindow(content, orient=VERTICAL)
# first pane, which would get widgets gridded into it:
f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)
f2 = ttk.Labelframe(p, text='Pane2', width=100, height=100)   # second pane
p.add(f1)
p.add(f2)

appHighlightFont = font.Font(family='Helvetica', size=12, weight='bold')
ttk.Label(root, text='Cuidadín!', font=appHighlightFont).grid(column=8, row=0, columnspan=2, sticky=(N, W), padx=5)

canvas = Canvas(content)
canvas.create_line(10, 10, 200, 50)

content.grid(column=0, row=0, sticky=(N, S, E, W))
#frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
n.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
p.grid(column=6, row=0, columnspan=2, sticky=(N, W), padx=5)

root.columnconfigure(0, weight=3)
root.rowconfigure(0, weight=1)

#content.columnconfigure(0, weight=3)
#content.columnconfigure(1, weight=3)
#content.columnconfigure(2, weight=3)
#content.columnconfigure(3, weight=1)
#content.columnconfigure(4, weight=1)
#content.rowconfigure(1, weight=1)

root.tk.call('tk', 'windowingsystem')     # will return x11, win32 or aqua

root.mainloop()