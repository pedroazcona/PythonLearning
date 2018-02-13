# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:42:36 2018

@author: poaa
"""

import tkinter as tk 
from tkinter import ttk 
from threading import Thread 
from urllib.request import urlretrieve, urlcleanup 


class Application(ttk.Frame): 
     
    def __init__(self, main_window): 
        super().__init__(main_window) 
        main_window.title("Barra de progreso en Tk") 
         
        self.progressbar = ttk.Progressbar(self) 
        self.progressbar.place(x=30, y=60, width=200) 
         
        self.download_button = ttk.Button( 
            self, text="Descargar", command=self.download_button_clicked) 
        self.download_button.place(x=30, y=20) 
        self.progres_label=ttk.Label(self, text='')
        self.progres_label.place(x=250, y=60) 
         
        self.place(width=300, height=200) 
        main_window.geometry("300x200") 
     
    def download(self): 
        url = "https://4.img-dpreview.com/files/p/TS5504x8256~sample_galleries/5682971467/6143475567.jpg" 
        urlretrieve(url, r'C:\Users\poaa\Documents\Python Scripts\Tkinter\foto.jpg', self.download_status) 
        urlcleanup() 
        self.progres_label['text']='Done'

     
    def download_button_clicked(self): 
        # Descargar el archivo en un nuevo hilo. 
        Thread(target=self.download).start() 
     
    def download_status(self, count, data_size, total_data): 
        if count == 0: 
            # Establecer el máximo valor para la barra de progreso. 
            self.progressbar.configure(maximum=total_data) 
        else: 
            # Aumentar el progreso. 
            self.progressbar.step(data_size) 
            self.progres_label['text']=str(int((self.progressbar['value']/self.progressbar['maximum'])*100))+'%'
 
main_window = tk.Tk() 
app = Application(main_window) 
app.mainloop() 
