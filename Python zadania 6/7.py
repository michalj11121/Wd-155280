import numpy as np

def foo(n):
    
    wynik = np.diag([2 for a in range(n)])
    for i in range(1,n):
        wynik += np.diag([2+2*i for a in range(n-i)],i)
    for i in range(1,n):
        wynik += np.diag([2+2*i for a in range(n-i)],-i)
    return wynik
print(foo(5))