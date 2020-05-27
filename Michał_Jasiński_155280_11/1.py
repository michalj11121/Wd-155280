import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

z=np.arange(0,2*np.pi,0.1)
x=np.sin(z)
y=2*(np.cos(z))
fig = plt.figure()
ax = fig.gca( projection = '3d' )


ax.plot(z, x, y, label = 'zadanie 1' )
ax.legend()
plt.show()