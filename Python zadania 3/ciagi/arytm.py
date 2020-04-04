def suma(a1=1,r=1,ile=10):
    wynik=0
    for i in range(0,ile):
        wynik=wynik+a1
        a1=a1+r
    return wynik


def ciag(a1=1,r=1,ile=10):
    wynik=0
    for i in range(0,ile):
        wynik=a1
        a1=a1+r
    return wynik
    
