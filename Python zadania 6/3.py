import numpy as np

def foo(n):
    x=np.zeros((n,n))
    pom=1
    for i in range(0,5):
        for j in range(0,5):
            x[i][j]=pom
            pom=pom+1

    return x
    
print(foo(5))

