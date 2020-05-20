import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.arange(1,21)





fig, ax = plt.subplots()
ax.plot(x,1/x,label='f(x) = 1/x')

ax.annotate('f(5)=0.2',
            xy=(5, 0.2), xycoords='data',
            xytext=(5,0.6), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.axis([1, len(x), 0, 1])
plt.show()


x=np.arange(0,30.1,0.1)
s=np.sin(x)
c=np.cos(x)
fig, ax = plt.subplots()
ax.plot(x,s,'-r',label='sin(x)')
ax.plot(x,c,'--b',label='cos(x)')
ax.annotate('sin(0)',
            xy=(0,0), xycoords='data',
            xytext=(0,-0.5), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

ax.annotate('cos(0)',
            xy=(0,1), xycoords='data',
            xytext=(0,0.5), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

plt.title("sin(x) i cos(x) dla x[0,30] z krokiem 0.1")
plt.xlabel('x')
plt.ylabel('sin(x) i cos(x)')
plt.xticks(np.arange(0,31))

plt.legend()
plt.show()