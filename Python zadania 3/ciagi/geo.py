def suma(a1=1,r=2,ile=10):
    wynik=1
    for i in range(0,ile):
        wynik=wynik+a1
        a1=a1*r
    return wynik


def ciag(a1=1,r=2,ile=10):
    wynik=1
    for i in range(0,ile):
        wynik=a1
        a1=a1*r
    return wynik

