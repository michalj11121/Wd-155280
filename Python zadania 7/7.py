import numpy as np

x=np.array((1,4,5,8,3,4)).reshape(2,3)
print(x)
a=np.sin(x)
y=np.array((1,4,5,8,3,4)).reshape(2,3)
print(y)
b=np.cos(y)
print(a+b)