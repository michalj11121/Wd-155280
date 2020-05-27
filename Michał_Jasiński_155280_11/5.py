import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
for jeden,dwa,trzy in [[121,0.25,False],[122,0.1,True]]:
    ax = fig.add_subplot( jeden , projection = '3d' )
    X = np.arange(- 5 , 5 , dwa )
    Y = np.arange(- 5 , 5 , dwa )
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X** 2 + Y** 2 )
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, cmap =plt.get_cmap('coolwarm'),
    linewidth = 0 , antialiased = trzy )
    ax.set_zlim(- 1.01 , 1.01 )
    ax.zaxis.set_major_locator(LinearLocator( 10 ))
    ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
    fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
plt.show()