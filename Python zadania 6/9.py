import numpy as np
x=np.arange(25)

for i in range (2,25):
    x[i]=x[i-2]+x[i-1]
mat = x.reshape((5,5))
print(mat)



