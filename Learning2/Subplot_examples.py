# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:55:10 2017

@author: poaa
"""
import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(0, 2*np.pi, 400)
#x = np.linspace(0, 20, 400)
x = np.arange(120).reshape((10, 12))
y = np.sin(x**2)

interp = 'bicubic'
fig, axs = plt.subplots(nrows=2, sharex=False, sharey=True,figsize=(3, 5))
axs[0].imshow(y, origin='lower', interpolation=interp)
axs[1].scatter(x,y)
