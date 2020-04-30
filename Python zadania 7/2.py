import numpy as np

a=np.arange(9).reshape(3,3)
b=np.arange(16).reshape(4,4)
print(a)
for i in range(0,3):
    print(f" rzad {a[i]}={a[i].min()}")
    print(f"kolumna {a[:,i]}={a[:,i].min()}")

print(b)
for i in range(0,4):
    print(f" rzad {b[i]}={b[i].min()}")
    print(f"kolumna {b[:,i]}={b[:,i].min()}")

print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))




