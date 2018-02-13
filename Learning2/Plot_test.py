# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:51:53 2017

@author: poaa
"""
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
#fig2 = plt.figure()
#ax = fig.add_subplot(1,1,1) # two rows, one column, first plot
#ax2 = fig2.add_subplot(1,1,1) # two rows, one column, first plot

rect = [1,1,1,1]
fig.add_axes(rect)
fig.add_axes(rect, frameon=False, facecolor='g')
fig.add_axes(rect, polar=True)
fig.add_axes(rect, projection='polar')
