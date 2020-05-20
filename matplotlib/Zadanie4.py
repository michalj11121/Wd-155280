import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
x=np.arange(0,30.1,0.1)
s=np.sin(x)
s2=np.sin(-x)

plt.plot(x,s+2,label='sin(x)')
plt.plot(x,s2,label='sin(x)')

plt.title("Wykres sin(x) i sin(x)")
plt.xlabel('x')
plt.ylabel('sin(x)')


plt.legend(loc=6)
plt.show()