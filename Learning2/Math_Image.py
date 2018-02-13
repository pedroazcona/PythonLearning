# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:38:33 2017

@author: poaa
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread(r'C:\Users\poaa\Documents\Python Scripts\Learning2\TestFiles\stinkbug.png')
imgplot = plt.imshow(img)
lum_img = img[:,:,0]
plt.imshow(lum_img, cmap="hot")
imgplot = plt.imshow(lum_img)
plt.colorbar()
imgplot.set_cmap('nipy_spectral')
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))
