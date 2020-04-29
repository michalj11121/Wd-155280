import numpy as np

def foo(n):
    pom=-np.arange(-n,0)
    wynik=np.diag(pom)
    return wynik

print(foo(5))
  

