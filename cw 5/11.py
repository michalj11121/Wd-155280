from itertools import  *

def fibo(a):
    pom=[0,1]
    
    for i in range(1,a+1):
        pom.append(pom[i]+pom[i-1])
        yield pom[i]
    

tmp=fibo(10)

print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
