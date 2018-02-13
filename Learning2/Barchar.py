# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:47:37 2017

@author: poaa
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 6

means_men = (20, 35, 30, 35, 27,12) #altura de la barra
std_men = (2, 3, 4, 1, 2, 6) #altura del palote, que nos marca el tamaño de la muestra

means_women = (25, 32, 34, 20, 25,32)
std_women = (3, 5, 2, 3, 3,3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25

opacity = 0.7
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='b',
                yerr=std_men, 
                error_kw=error_config,
                label='Men')

rects2 = ax.bar(index + bar_width, means_women, bar_width,
                alpha=opacity, color='r',
                yerr=std_women, 
                error_kw=error_config,
                label='Women')

ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo','Jurnio'))
ax.legend()

fig.tight_layout()
plt.show()
