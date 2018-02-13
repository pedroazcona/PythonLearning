# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:38:33 2017

@author: poaa
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

img=Image.open(r'C:\Users\poaa\Documents\Python Scripts\Learning2\TestFiles\stinkbug.png')
img.thumbnail((64, 64), Image.ANTIALIAS) # resizes image in-place
imgplot = plt.imshow(img, interpolation="bicubic")
