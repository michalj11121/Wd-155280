import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19634822 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin




fig = plt.figure()
ax = fig.add_subplot( projection = '3d' )

xs = randrange(20, 0 , 100 )
ys = randrange(20, 0 , 100 )

ax.scatter(xs, ys, 0, c ='red', marker ='o')
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
xs = [0,25,25,80,80]
ys = [0,0,70,70,90]
zs = 0
ax.plot(xs, ys, zs, c ='green')
ax.set_zlim(0 , 1 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )

plt.show()