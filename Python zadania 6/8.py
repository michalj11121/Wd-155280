import numpy as np
def foo(tab,n):
    
    x=int(tab.shape[0]/2)
    y=int(tab.shape[1]/2)
    
    if n=="poziomo":
        if tab.shape[0]%2!=0:
            return "zle wymiary"
        elif tab.shape[0]%2==0:
            return tab[0:x]

    if n=="pionowo":
        if tab.shape[1]%2!=0:
            return "zle wymiary"
        elif tab.shape[1]%2==0:
            return tab[0::,0:y]
    

x=np.zeros((6,6))
print(foo(x,'poziomo'))
print(foo(x,'pionowo'))
y=np.zeros((10,10))
print(foo(y,'poziomo'))
print(foo(y,'pionowo'))
z=np.zeros((7,7))
print(foo(z,'poziomo'))
print(foo(z,'pionowo'))