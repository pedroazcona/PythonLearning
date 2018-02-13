# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:51:53 2018

@author: poaa
"""
from tkinter import *
from tkinter import ttk

root = Tk()
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
root.grid_columnconfigure(0, weight=1)
ttk.Sizegrip(root).grid(column=999, row=999, sticky=(S,E))
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()