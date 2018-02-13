# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:02:35 2018

@author: poaa
"""

from tkinter import *
from tkinter import ttk 
from tkinter import filedialog, colorchooser, messagebox



root = Tk()
root.option_add('*tearOff', FALSE)

#filename = filedialog.askopenfilename()
#colorchooser.askcolor(initialcolor='#ff0000')
#messagebox.showinfo(message='Have a good day')
messagebox.askyesno(message='Are you sure you want to install SuperVirus?', icon='error',title='Install')

root.mainloop()