# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:27:45 2017

@author: poaa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:54:18 2017

@author: poaa
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 250

#ells = [Ellipse(xy=np.random.rand(2) * 10,
#                width=np.random.rand(), height=np.random.rand(),
#                angle=np.random.rand() * 360)
#        for i in range(NUM)]

ells=[Ellipse(xy=[10,10],
                width=15, 
                height=10,
                angle=45)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
#    e.set_alpha(np.random.rand()) #0 transparente, 1 opaco
    e.set_alpha(.75) #0 transparente, 1 opaco
#    e.set_facecolor(np.random.rand(3)) #RGB Color (rango entre 0 y 1)
    e.set_facecolor([0.25,0.65,0.25])

ax.set_xlim(0, 30)
ax.set_ylim(0, 30)

plt.show()
