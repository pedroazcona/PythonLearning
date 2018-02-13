# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:18:21 2018

@author: poaa
"""

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
#        pass
        print(sys.call_tracing())
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="12 12 12 12") #izq, arriba, drch, abajo
mainframe['padding'] = (6,12) # lo mismo pero izq/drch, arriba/abajo
mainframe['borderwidth'] = 2
mainframe['relief'] = 'raised'
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

phone = StringVar()
home = ttk.Radiobutton(mainframe, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(mainframe, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(mainframe, text='Mobile', variable=phone, value='cell')


countryvar = StringVar()
country = ttk.Combobox(mainframe, textvariable=countryvar)
country['values'] = ('USA', 'Canada', 'Australia')

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
