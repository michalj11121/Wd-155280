import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
x=np.arange(0,30.1,0.1)
s=np.sin(x)
c=np.cos(x)
plt.plot(x,s,'-r',label='sin(x)')
plt.plot(x,c,'--b',label='cos(x)')
plt.title("sin(x) i cos(x) dla x[0,30] z krokiem 0.1")
plt.xlabel('x')
plt.ylabel('sin(x) i cos(x)')
plt.xticks(np.arange(0,31))

plt.legend()
plt.show()