# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 08:23:45 2017

@author: poaa
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dates = pd.date_range('20170101', periods=100)
x = np.random.randn(100)
#datos = [[x],[x**2], [np.sin(x)]]
#df = pd.DataFrame(datos, index=dates, columns=['Value','Square','Sin'])
df = pd.DataFrame({'Value': x,
                   'Square': x**2,
                   'Sin': np.sin(x) }, index=dates)
json = df.to_json()
htlm = df.to_html()

Html_file= open(r'C:\Users\poaa\Documents\Python Scripts\Learning2\prueba.html',"w")
Html_file.write(htlm)
Html_file.close()

