# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:27:05 2017

@author: poaa
"""

import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import pandas as pd
import numpy as np

Pandemia = pd.read_csv(r'C:\Users\poaa\Documents\PENTAHO_TEST\test_result.txt', sep=';')

#B= list(Pandemia.price)
#A= [B,B,B,B]
A = np.random.rand(10, 10)
#print (A)

fig, axs = plt.subplots(1, 3, figsize=(10, 3))
for ax, interp in zip(axs, ['nearest', 'bilinear', 'bicubic' ]):
    ax.imshow(A, interpolation=interp)
    ax.set_title(interp.capitalize())
    ax.grid(True)

#plt.show()
