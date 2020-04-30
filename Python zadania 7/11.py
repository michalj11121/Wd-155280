import numpy as np 
a=np.arange(12)
b=np.arange(12)
c=np.arange(12)
print(a)
print(b)
print(c)
a=a.reshape(3,4)
b=b.reshape(4,3)
b=b.reshape(2,6)    
print(a.ravel())
print(b.ravel())
print(c.ravel())
#sa identyczne