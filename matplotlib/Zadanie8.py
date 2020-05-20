import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def rzut(n):
    tab=np.array([(np.random.randint(6)+1)+(np.random.randint(6)+1) for x in range(n)])
    return tab
    
    

temp=rzut(100)
plt.hist(temp,bins=10,facecolor='red',alpha=0.75)
plt.xlabel('Wartości')
plt.ylabel('Ilość rzutów o danej sumie')
plt.title('Histogram')
plt.grid(True)  
plt.show()
     



