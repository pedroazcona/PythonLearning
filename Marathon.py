# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:01:07 2018

@author: poaa
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:56:11 2017

@author: poaa
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import radviz



Maraton = pd.read_csv(r'C:\Users\poaa\Documents\Python Scripts\Learning2\Maraton_Data\ResultsMaratonAll.csv', sep=';')

#print(Maraton.index)
#print(Maraton.columns)
#print(Maraton.describe())

data = pd.DataFrame(Maraton, columns=['Year', 'Pos','Minutes_Real','Categoria'] )
data['Minutes_Real']=data['Minutes_Real'].str.replace(',','.') #cambiamos , por . para decimales
data['Minutes_Real']=[float(x) for x in data['Minutes_Real']]

#data['Minutes_Real']=

#data_2015_M = data.query('Year == 2015 and Categoria=="SENIOR MASCUL"')
#data_2015_M = data.query('Year == 2015')
#data_2015_M2 = data[data.Year == 2015]
#print(data_2015_M.head())

#print(np.round(data_2015['Minutes_Real']))

#print(data_2015.describe())
#data_2015.plot(kind='kde', x=data_2015.index, y='Minutes_Real')
#data_2015.plot(kind='bar', x=data_2015.index, y='Minutes_Real')

#plt.plot.scatter(x=data_2015.index, y='Minutes_Real', label='Categoria', data=data_2015_M, cmap='viridis')


#data2 = pd.DataFrame(Maraton, columns=['Year', 'Categoria'] )
#print(data2.tail())
#print(data2[data2.Year==2015])
#print (data2.Year)

#data.Year.value_counts()#.plot()

#data2.plot(kind='hist',x=data2.index, y='Categoria')
#c=data2.groupby(['Categoria'])
plt.rcParams["figure.figsize"] = [10,10]
c=pd.DataFrame([int(x) for x in data.Minutes_Real]).groupby(0).size()
data.plot(kind='scatter',x='Year',y='Minutes_Real', s=c, ylim=100)







