import numpy as np 
x=np.arange(81).reshape(9,9)
print(x)
x=x.ravel()
print(x)
x=x.reshape(9,9)
print(x)
x=x.transpose()
print(x)

# mamy malo mozliwosci poniewaz inny a x a nie da 81 tylko 9 x 9 