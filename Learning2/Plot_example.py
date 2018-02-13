import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import pandas as pd
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

iris = pd.read_csv(r'C:\Users\poaa\Documents\Python Scripts\iris.txt', sep=',')
l=list(iris.sepal_length)
w=list(iris.sepal_width)

fig, ax = plt.subplots()
ax.plot(l,w)

ax.set(xlabel='Length', ylabel='Width',
       title='Sepal Plot')
ax.grid()

fig.savefig(r'C:\Users\poaa\Documents\Python Scripts\Learning2\TestFiles\Plot2.png')
#fig.savefig(r'C:\Users\poaa\Documents\Python Scripts\Learning2\TestFiles\Plot2.pdf')

x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('blue should be up')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('blue should be down')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
