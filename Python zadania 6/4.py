import numpy as np
def foo(n,m):
    wynik=np.logspace(1,m, num=m, base=n)
    return wynik
print(foo(10,3))
print(foo(2,8))
print(foo(3,5))
