# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:56:59 2017

@author: poaa
"""

import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(5), #X
        'c': np.random.randint(0, 50, 5),
        'd': np.random.randn(5)}
#data['b'] = data['a'] + 10 * np.random.randn(5)  #Y
data['b'] = 10 * np.random.randn(5) #Y
data['d'] = np.abs(data['d']) * 100 #Cantidad de Y´s

print(data)

plt.scatter('a', 'b', c='c', s='d', data=data, cmap='viridis')
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
