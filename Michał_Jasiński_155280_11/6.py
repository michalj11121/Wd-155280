import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19680822 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin




fig = plt.figure()

ax = fig.add_subplot( 121 , projection = '3d' )

xs = randrange(20, 0 , 100 )
ys = randrange(20, 0 , 100 )
zs = randrange(20, 0 , 100 )
ax.scatter(xs, ys, zs, c ='red', marker ='>')
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

ax = fig.add_subplot( 122 , projection = '3d' )

xs = randrange(5, 0 , 100 )
ys = randrange(5, 0 , 100 )
zs = randrange(5, 0 , 100 )
ax.plot(xs, ys, zs, c ='red', marker ='>',linestyle='--')
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

plt.show()